
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):

    app_name: str = "SupportDesk API"
    app_version: str = "1.0.0"
    app_description: str = (
        "Enterprise Customer Support and Ticket Management Platform"
    )

    debug: bool = True

    #Database configuration
    db_host:str = "localhost"
    db_port:int = 5432
    db_name:str = "supportdesk_db"
    db_user:str = "postgres"
    db_password : SecretStr
    
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
