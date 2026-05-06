import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    """This function builds the connection with DB"""

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

def save_url (original_url, short_code):
    """This function saves URL data into the DB"""
    
    db_connection = get_connection()
    cursor = db_connection.cursor()
    # %s are placeholders, replaced with actual values. These are used to avoid SQL injection.
    cursor.execute("INSERT INTO urls(original_url, short_code) VALUES (%s, %s)", (original_url, short_code))
    db_connection.commit()
    cursor.close()
    db_connection.close()

def get_original_url(short_code):
    db_connection = get_connection()
    cursor = db_connection.cursor()
    # Reason for this , (short_code,) is that Python could treat it as tuple; because that is what psycopg2 expects
    cursor.execute("SELECT original_url FROM urls WHERE short_code=(%s)", (short_code,))
    result = cursor.fetchone()
    url_result = result[0]
    return url_result

if __name__ == "__main__":
    save_url("https://www.psycopg.org/docs/index.html", "ab123")
    print("URL saved successfully!")

    get_original_url("ab123")
    print("Data Fetched successfully...")


