from src.config import *
from src.models import Users, Sessions, Messages, Base

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


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

