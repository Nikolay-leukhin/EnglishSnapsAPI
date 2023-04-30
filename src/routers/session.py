from fastapi import APIRouter
from ..schemas.session import ModelSessionSend
from ..database import query_add_session

router = APIRouter()


@router.post('/session/add_session')
async def add_session(request: ModelSessionSend):
    query_add_session(**request.__dict__)
    return {'code': 222, 'msg': 'ok'}

