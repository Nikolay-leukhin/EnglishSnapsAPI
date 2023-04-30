from src.config import *
from src.models import Users, Sessions, Messages

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

try:
    DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(DB_URL)
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


def query_add_session(**request):
    with SQLSession() as session:
        session_to_add = Sessions(**request)
        session.add(session_to_add)
        session.commit()


def query_add_message(**request):
    with SQLSession() as session:
        session_to_add = Messages(**request)
        session.add(session_to_add)
        session.commit()


# спокойноно можно брать обычные сессии не асинхронные
# TODO: о боте. в комит на базу стоит собирать сразу два сообщения от ЮЗЕРА и от БОТА. это ускорит процесс а функция которая делала это возвращала сам респонс бота
# TODO: как вариант можно  бать лишь последние 4 или 6 сообщений между ботом и ползователем как история сообщений для большей производительности
# TODO: интересно было бы реализовать систему, лайков и дизлайков на сообщение. чтобы потом ИСХОДЯ ОТ ИНТЕРЕСОВ ПОЛЬЗОВАТЕЛЯ  задать некоторый ситемный параметр
# TODO: можно юзать без редиски
# TODO: в обьекте message стоит хранить не время а порядок сообщения ауф