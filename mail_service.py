from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pathlib import Path
from pydantic import EmailStr
from schema import EmailSchema
from settings import settings


class EmailService:
    def __init__(self):
        conf = ConnectionConfig(
            MAIL_USERNAME=settings.MAIL_USERNAME,
            MAIL_PASSWORD=settings.MAIL_PASSWORD,
            MAIL_FROM=settings.MAIL_FROM,
            MAIL_PORT=settings.MAIL_PORT,
            MAIL_SERVER=settings.MAIL_SERVER,
            MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
            MAIL_TLS=settings.MAIL_TLS,
            MAIL_SSL=settings.MAIL_SSL,
            USE_CREDENTIALS=settings.USE_CREDENTIALS,
            VALIDATE_CERTS=settings.VALIDATE_CERTS,
            TEMPLATE_FOLDER=Path(settings.BASE_DIR, 'templates'),
        )
        self.fast_mail = FastMail(conf)

    async def send_mail(self, subject: str, schema: EmailSchema, template: str):
        message = MessageSchema(
            subject=subject,
            recipients=[schema.email],  # List of recipients, as many as you can pass
            template_body=schema.body,
            subtype='html',
        )
        await self.fast_mail.send_message(
            message,
            template_name=template
        )

    async def send_file(self, subject: str, email: EmailStr, body: str):
        message = MessageSchema(
            subject=subject,
            recipients=[email],  # List of recipients, as many as you can pass
            html=body,
            subtype='html',
        )
        await self.fast_mail.send_message(message)


service = EmailService()


