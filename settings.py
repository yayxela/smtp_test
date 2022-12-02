import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    BASE_DIR: str = os.getenv('BASE_DIR', '')

    MAIL_USERNAME: str = os.getenv('MAIL_USERNAME', '')
    MAIL_PASSWORD: str = os.getenv('MAIL_PASSWORD', '')
    MAIL_FROM: str = os.getenv('MAIL_FROM', '')
    MAIL_PORT: int = os.getenv('MAIL_PORT', '')
    MAIL_SERVER: str = os.getenv('MAIL_SERVER', '')
    MAIL_FROM_NAME: str = os.getenv('MAIL_FROM_NAME', '')
    MAIL_TLS: bool = os.getenv("MAIL_TLS", 'False').lower() in ('true', '1', 't')
    MAIL_SSL: bool = os.getenv("MAIL_SSL", 'False').lower() in ('true', '1', 't'),
    USE_CREDENTIALS: bool = os.getenv("USE_CREDENTIALS", 'False').lower() in ('true', '1', 't'),
    VALIDATE_CERTS: bool = os.getenv("VALIDATE_CERTS", 'False').lower() in ('true', '1', 't'),

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
