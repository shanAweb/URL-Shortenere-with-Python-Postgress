import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
def get_connection():
    """ This function builds the connection with DB"""

    host = os.getenv("DB_HOST", "DB host was not provided")
    dbname = os.getenv("DB_NAME", "DB Name was not provided")
    port = os.getenv("DB_PORT", "DB port was not provided")
    user = os.getenv("DB_USER", "DB user was not provided")
    password = os.getenv("DB_PASSWORD", "DB password was not required")
    connection = psycopg2.connect(
        host = host,
        dbname = dbname,
        port = port,
        user = user,
        password = password
    )
    return connection

print (get_connection() )



