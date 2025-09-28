# Configuration file with classes "settings" and "databaseSettings" for calls and connections 

import os
from dotenv import load_dotenv 

load_dotenv()

# from config import settings

class Settings:
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    CHANNEL_LINK = os.environ.get("CHANNEL_LINK")
    YOUTUBE_LINK = os.environ.get("YOUTUBE_LINK")
    LEAD_ADMIN_USERNAME = os.environ.get("LEAD_ADMIN_USERNAME")
    CONTACT_ADMIN_USERNAME = os.environ.get("CONTACT_ADMIN_USERNAME")

settings = Settings()

# from config impoort IDSettings

class IDSettings:
    LEAD_ADMIN_ID = os.environ.get("LEAD_ADMIN_ID")
    ADMIN_ID  = os.environ.get("ADMIN_ID")
    
IDsettings = IDSettings()

# from config import databaseSettings

class DatabaseSettings:
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD") 
    POSTGRES_USER = os.environ.get("POSTGRES_USER")
    POSTGRES_DB = os.environ.get("POSTGRES_DB")
    POSTGRES_PORT_NUMBER = os.environ.get("POSTGRES_PORT_NUMBER")
    POSTGRES_HOST = os.environ.get("POSTGRES_HOST")

databaseSettings = DatabaseSettings()