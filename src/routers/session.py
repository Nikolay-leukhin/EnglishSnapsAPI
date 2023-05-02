from fastapi import APIRouter

from ..schemas.message import ModelMessageSend
from ..schemas.session import ModelSessionSend
from ..database import query_add_session, query_get_all_user_sessions, query_get_english_level, query_add_message

from ..schemas.message import BotRoles

router = APIRouter()


@router.post('/session/add_session')
async def add_session(request: ModelSessionSend):
    # TODO при добавлении сессии нужно отправлять message от system  с названием фв
    # TODO с названием сесии как некотопрый заголовок темы
    user_id: int = request.__dict__.pop('user_id')
    user_english_level = query_get_english_level(user_id=user_id)
    response_add_session = query_add_session(**request.__dict__)
    system_msg: ModelMessageSend = ModelMessageSend(
        user_id=user_id,
        session_id=response_add_session.id,
        message_order=0,
        message_text=f'you helps to learn english. current theme of dialog is {response_add_session.session_name}. user english level A1',
        sender=BotRoles.system,
    )
    query_add_message(**system_msg.__dict__)
    return {
        'code': 200,
        'session': response_add_session
    }


@router.get('/session/user_session/{user_id}')
async def get_session(user_id: int):
    response = query_get_all_user_sessions(user_id)
    return response
