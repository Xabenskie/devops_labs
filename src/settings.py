from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SERVER_ADDR: str = "0.0.0.0"
    SERVER_PORT: int = 8080
    
settings = Settings()