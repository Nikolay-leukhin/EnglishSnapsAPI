from typing import List

from src.config import *
from src.models import Users, Sessions, Messages, Base, UserWord, Word, Theme

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from src.schemas.theme import ThemeModel
from src.schemas.word import WordModel

try:
    DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(DB_URL)
    print('connection secces')
except Exception as ex:
    raise ex


SQLSession = sessionmaker(bind=engine)


def get_users():
    with SQLSession() as session:
        users = session.query(Users).all()
        return users


def query_add_user(**request):
    with SQLSession() as session:
        user_to_add = Users(**request)
        session.add(user_to_add)
        session.commit()
        session.refresh(user_to_add)
        return user_to_add


def query_add_session(**request):
    with SQLSession() as session:
        session_to_add = Sessions(**request)
        session.add(session_to_add)
        session.commit()
        session.refresh(session_to_add)
        return session_to_add


def query_add_message(**request):
    with SQLSession() as session:
        session_to_add = Messages(**request)
        session.add(session_to_add)
        session.commit()


def query_get_latest_msgs(quantity, user: int, session_num: int):
    with SQLSession() as session:
        results = session.query(Messages).where(Messages.sender != 'system').filter_by(
            user_id=user,
            session_id=session_num
        ).order_by(Messages.message_order).limit(quantity).all()
        return results


def query_get_all_user_sessions(user_id: int):
    with SQLSession() as session:
        results = session.query(Sessions).join(Messages).filter(Messages.user_id == user_id).all()
        return results


def query_is_user_exist(email: str, password: str):
    with SQLSession() as session:
        user = session.query(Users).filter_by(
            email=email,
            password=password
        ).first()
    return {
        'is_exist': bool(user),
        'user': user
    }


def query_get_english_level(user_id: int):
    with SQLSession() as session:
        result = session.query(Users.english_level).filter_by(
            id=user_id
        ).first()
        return str(result)


def query_get_theme_words(theme_id: int) -> List[WordModel]:
    with SQLSession() as session:
        raw_data = session.query(Word).filter_by(
            theme_id=theme_id
        ).all()
        if len(raw_data) == 0:
            return []

        data: list[WordModel] = [
            WordModel(
                id=item.id,
                name=item.name,
                explanation=item.explanation,
                translation=item.translation,
                transcription=item.transcription,
                theme_id=item.theme_id
            ) for item in raw_data
        ]
        return data


def query_add_theme(data: ThemeModel):
    with SQLSession() as session:
        try:
            tables = Theme(
                theme_name=data.theme_name
            )
            req = session.add(tables)
            session.commit()
            session.refresh(tables)
        except Exception as ex:
            return None
        return tables