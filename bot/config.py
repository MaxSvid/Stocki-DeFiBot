# Configuration file with classes "Settings" and "DatabaseSettings"

import os
from dotenv import load_dotenv 

load_dotenv()

# from bot.config import settings

class Settings:
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    REVIEWS_CHANNEL_LINK = os.environ.get("REVIEWS_CHANNEL_LINK")
    ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME")

settings = Settings()

# from bot.config import databaseSettings

class DatabaseSettings:
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD") 
    POSTGRES_USER = os.environ.get("POSTGRES_USER")
    POSTGRES_DB = os.environ.get("POSTGRES_DB")
    POSTGRES_PORT_NUMBER = os.environ.get("POSTGRES_PORT_NUMBER")
    POSTGRES_HOST = os.environ.get("POSTGRES_HOST")

databaseSettings = DatabaseSettings()