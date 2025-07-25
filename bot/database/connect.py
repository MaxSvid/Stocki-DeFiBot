# Configuration file with classes "DatabaseSettings" from config.py for database connection

# https://www.geeksforgeeks.org/python/python-psycopg-connection-class/

from psycopg import connect, OperationalError
from bot.config import databaseSettings


def create_connection():
    connection = None 
    try:
        connection = connect(
            dbname=databaseSettings.POSTGRES_DB,
            user=databaseSettings.POSTGRES_USER,
            password=databaseSettings.POSTGRES_PASSWORD,
            host=databaseSettings.POSTGRES_HOST,
            port=databaseSettings.POSTGRES_PORT_NUMBER
        )
        print("Connection to PostgreSQL DB successful") 
    except OperationalError as e:
        print(f"Can't connect to PostgreSQL server: {e}")
    
    return connection    

