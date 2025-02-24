from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    sqlalchemy_string: str = os.getenv("POSTGRES_URI")
    
settings = Settings()