from sqlalchemy import Column, Integer, String, Boolean, DateTime, MetaData, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

from datetime import datetime


Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    nickname: str = Column(String(20), nullable=False)
    password: str = Column(String, nullable=False)
    avatar_path: str = Column(String(20), nullable=True)
    email: str = Column(String, nullable=False)
    phone: str = Column(String(20), nullable=True)
    vk_contact: str = Column(String, nullable=True)
    tg_contact: str = Column(String, nullable=True)
    longitude: str = Column(String)
    latitude: str = Column(String)
    english_level: str = Column(String, nullable=True)
    role: str = Column(String, nullable=True)
    is_active: bool = Column(Boolean, nullable=False)
    is_superuser: bool = Column(Boolean, nullable=False)


class Sessions(Base):
    __tablename__ = 'sessions'
    id: int = Column(Integer, primary_key=True)
    session_name: str = Column(String, nullable=False)
    is_ended: bool = Column(Boolean, nullable=False, default=False)
    created_at: datetime = Column(DateTime(), default=datetime.now)


class Messages(Base):
    __tablename__ = 'messages'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    session_id = Column(Integer, ForeignKey('sessions.id'))
    message_order: int = Column(Integer, nullable=False)
    message_text: str = Column(String, nullable=False)
    sender: str = Column(String, nullable=False)

    rel_users = relationship('Users', backref='messages')
    rel_sessions = relationship('Sessions', backref='messages')


class Word(Base):
    __tablename__ = 'word'
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False)
    explanation: str = Column(String, nullable=False)
    translation: str = Column(String, nullable=False)
    transcription: str = Column(String, nullable=False)
    theme_id: int = Column(Integer, ForeignKey('theme.id'))

    res_theme = relationship('Theme', backref='word')


class Theme(Base):
    __tablename__ = 'theme'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    theme_name: str = Column(String, nullable=False)


class UserWord(Base):
    __tablename__ = 'users_words'

    id: int = Column(Integer, primary_key=True)
    user_id: int = Column(Integer, ForeignKey('users.id'))
    word_id: int = Column(Integer, ForeignKey('word.id'))
    is_learned: bool = Column(Boolean, nullable=False)

    rel_users = relationship('Users', backref='users_words')
    rel_word = relationship('Word', backref='users_words')