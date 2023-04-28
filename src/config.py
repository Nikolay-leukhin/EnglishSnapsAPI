import os

from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.environ.get('DB_NAME')
DB_PWD = os.environ.get('DB_PWD')
DB_USER = os.environ.get('DB_USER')
DB_PORT = os.environ.get('DB_PORT')
DB_HOST = os.environ.get('DB_HOST')
