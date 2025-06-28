# Configuration file with classes "DatabaseSettings" from config.py for database connection

from psycopg import connect, OperationalError
from bot.config import databaseSettings

# def create_connection():
