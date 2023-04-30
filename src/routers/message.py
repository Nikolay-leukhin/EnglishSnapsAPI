from fastapi import APIRouter

from ..database import query_add_message
from ..schemas.message import ModelMessageSend

router = APIRouter()


@router.post('/message/add_message')
async def add_message(request: ModelMessageSend):
    query_add_message(**request.__dict__)
    return {
        'code': 123,
        'msg': 'sex msg'
    }
