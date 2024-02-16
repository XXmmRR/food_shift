from decouple import config
from pydantic import BaseModel


class Settings(BaseModel):
    """Server config settings."""

    root_url: str = config("ROOT_URL", default="http://localhost:8080")

    # Security settings
    authjwt_secret_key: str = config("SECRET_KEY")
    salt: bytes = config("SALT").encode()
    # FastMail SMTP server settings
    mail_console: bool = config("MAIL_CONSOLE", default=False, cast=bool)
    mail_server: str = config("MAIL_SERVER", default="smtp.gmail.com")
    mail_port: int = config("MAIL_PORT", default=587, cast=int)
    mail_username: str = config("MAIL_USERNAME", default="")
    mail_password: str = config("MAIL_PASSWORD", default="")
    mail_sender: str = config("MAIL_SENDER", default="")

    testing: bool = config("TESTING", default=False, cast=bool)

    # Mongo settings
    MONGODB_URL: str = config("MONGODB_URL")
    MIN_CONNECTIONS_COUNT: int = config("MIN_CONNECTIONS_COUNT")
    MAX_CONNECTIONS_COUNT: int = config("MAX_CONNECTIONS_COUNT")


CONFIG = Settings()
