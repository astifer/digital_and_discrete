from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000

    group_key: str
    keyboard_key: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


config = Settings()