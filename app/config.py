from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_password : str
    database_hostname : str = "postgres"
    database_port : str = "5432"
    database_name: str
    database_username: str

    secret_key: str
    algorithm: str
    access_token_Expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()

