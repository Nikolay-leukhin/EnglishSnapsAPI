from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(256), nullable=False)
    email: str = Column(String(256), nullable=False)
    profession: str = Column(String(256), nullable=False)


