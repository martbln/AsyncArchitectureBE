import os
import secrets

from pydantic import BaseSettings


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


class Settings(BaseSettings):
    # GENERAL
    ENV: str = ''
    SECRET_KEY: str = secrets.token_urlsafe(32)
    PROJECT_NAME: str = 'PopugUber'

    # API
    API_STR: str = '/api'

    class Config:
        case_sensitive = True


settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
