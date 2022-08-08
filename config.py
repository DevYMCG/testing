import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

class Settings:
    TITLE="Title comming from config file"
    VERSION="0.0.1"
    DESCRIPTION="""
    this is dummy project
    this is not for production
    description is coming from config file
    """
    NAME = "Yohana Contreras"
    EMAIL = "yohana.contrerasg@gmail.com"

    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE", "mydb")
    DATABASE_URL = F"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"

setting = Settings()