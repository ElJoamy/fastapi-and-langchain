from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import cache

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')
    
    api_name: str = "LanchChain using FastAPI"
    revision: str = "local"
    gpt: str = "gpt-3.5-turbo-1106"
    log_level: str = "DEBUG"
    api_url: str = "http://localhost:8000/"
    api_key:str

@cache
def get_settings():
    print("getting settings...")
    return Settings()