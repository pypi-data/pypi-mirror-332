import time

import requests
from pydantic import BaseModel, ConfigDict, validator
from tqdm.auto import tqdm

from pytanis.config import Config, get_cfg


class MetaData(BaseModel):
    """Additional, arbitrary metadata provided by the user like for template filling"""

    model_config = ConfigDict(extra='allow')


class Recipient(BaseModel):
    """Details about the recipient

    Use the `data` field to store additional information
    """

    name: str
    email: str
    address_as: str | None = None  # could be the first name
    data: MetaData | None = None

    # TODO[pydantic]: We couldn't refactor the `validator`, please replace it by `field_validator` manually.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-validators for more information.
    @validator('address_as')
    @classmethod
    def fill_with_name(cls, v, values):
        if v is None:
            v = values['name']
        return v


class Mail(BaseModel):
    """Mail template

    Use the `data` field to store additional information

    You can use the typical [Format String Syntax] and the objects `recipient` and `mail`
    to access metadata to complement the template, e.g.:

    ```
    Hello {recipient.address_as},

    We hope it's ok to address you your first name rather than using your full name being {recipient.name}.
    Have you read the email's subject '{mail.subject}'? How is your work right now at {recipient.data.company}?

    Cheers!
    ```

    [Format String Syntax]: https://docs.python.org/3/library/string.html#formatstrings
    """

    subject: str
    body: str
    recipients: list[Recipient]
    data: MetaData | None = None


class MailClient:
    """Mail client for mass mails via Mailgun"""

    batch_size: int = 10  # n messages are a batch
    wait_time: int = 20  # wait time after eacht batch before next
    timeout: int = 10  # timeout for requests in seconds

    def __init__(self, config: Config | None = None):
        if config is None:
            config = get_cfg()
        self._config = config

    # TODO: Check return type of mail
    def send(self, mail: Mail):
        """Send a mail to all recipients using Mailgun"""
        errors = []
        responses = []

        # TODO: improve Mailgun batch mailing by setting custom transactional variables
        for idx, recipient in enumerate(tqdm(mail.recipients), start=1):
            try:
                recipient_mail = mail.model_copy()
                if self._config.Mailgun.token is None:
                    msg = 'API token for Mailgun is empty'
                    raise RuntimeError(msg)
                if self._config.Mailgun.from_address is None:
                    msg = 'From Email for Mailgun is empty'
                    raise RuntimeError(msg)
                if self._config.Mailgun.reply_to is None:
                    msg = 'Reply To Email for Mailgun is empty'
                    raise RuntimeError(msg)

                response = requests.post(
                    'https://api.eu.mailgun.net/v3/mg.pycon.de/messages',
                    auth=('api', self._config.Mailgun.token),
                    data={
                        'to': [recipient.email],
                        'from': self._config.Mailgun.from_address,
                        'subject': recipient_mail.subject.format(recipient=recipient, mail=mail),
                        'text': recipient_mail.body.format(recipient=recipient, mail=mail),
                        'h:Reply-To': self._config.Mailgun.reply_to,
                    },
                    timeout=self.timeout,
                )
                # check response status message and throw exception if not 200
                response.raise_for_status()
            except Exception as e:
                errors.append((recipient, e))
            else:
                responses.append(response)

            if idx % self.batch_size == 0:
                time.sleep(self.wait_time)

        return responses, errors
