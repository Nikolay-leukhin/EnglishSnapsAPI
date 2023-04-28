from config import *
from models import User


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DB_URL)

SQLSession = sessionmaker(bind=engine)


def get_users():
    with SQLSession() as session:
        users = session.query(User).all()
        return users
