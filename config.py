import os
from dotenv import load_dotenv

load_dotenv() 

SECRET_KEY = os.environ.get("JWT_SECRET", "ByteMenu#default") 
JWT_ALGORITHM = "HS256"

DATABASE_PATH = "database.sqlite3" 

HOST = "localhost"
PORT = 5001
DEBUG = True
RELOADER = True