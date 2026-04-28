# import psycopg2-binary
import os
from dotenv import load_dotenv

# Loading .env varaiables for DB credientiels
DB_HOST = "DB_HOST"
DB_PORT = "DB_PORT"
DB_NAME = "DB_NAME"
DB_USER = "DB_USER"
DB_PASSWORD = "DB_PASSWORD"

load_dotenv()
print (os.getenv(DB_HOST, "DB host was not provided"))
print (os.getenv(DB_NAME, "DB Name was not provided"))
print (os.getenv(DB_PORT, "DB port was not provided"))
print (os.getenv(DB_USER, "DB user was not provided"))
print (os.getenv(DB_PASSWORD, "DB password was not required"))
# print(os.getenv(""))

