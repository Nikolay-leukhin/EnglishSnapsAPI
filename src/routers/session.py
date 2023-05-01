from fastapi import APIRouter
from ..schemas.session import ModelSessionSend
from ..database import query_add_session, query_get_all_user_sessions

router = APIRouter()


@router.post('/session/add_session')
async def add_session(request: ModelSessionSend):
    query_add_session(**request.__dict__)
    return {'code': 222, 'msg': 'ok'}


@router.get('/session/user_session/{user_id}')
async def get_session(user_id: int):
    response = query_get_all_user_sessions(user_id)
    return response
