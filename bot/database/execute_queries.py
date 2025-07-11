"""
It is best to use pgAdmin for queries (localhost5050:80)
Still good idea to use:
docker-compose exec postgres psql -U POSTGRES_USER -d POSTGRES_DB 
"""

from bot.database.connect import create_connection
from psycopg import OperationalError

def execute_query(connection, query: str):
    connection.autocommit = True 
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            print("Query executed successfully")
    except OperationalError as e:
        print(f"Query error: {e}")

def execute_read_query(connection, query: str):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")
        return None 

if __name__ == "__main__": 
    connection = create_connection()
    if connection:
        write_query = ""
        if write_query:
            execute_query(connection, write_query)

    read_query = ""
    if read_query:
        result = execute_read_query(connection, read_query)
        if result: 
            print("Query results:", result)

    connection.close()