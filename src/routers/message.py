from fastapi import APIRouter

from ..ai_bot.bot import BotAssistant

from ..database import query_add_message, query_get_latest_msgs
from ..schemas.message import ModelMessageSend

router = APIRouter()


@router.post('/message/add_message')
async def add_message(request: ModelMessageSend):
    bot_response = BotAssistant(request.__dict__).make_bot_request()
    query_add_message(**request.__dict__)
    query_add_message(**bot_response)
    return bot_response


@router.get('/message/get_messages')
async def get_latest_messages(user_id: int, session_id: int, quantity: int = None):
    """quantity 0 - get all messages / > 0 some quantuty of messages"""
    response = query_get_latest_msgs(quantity, user_id, session_id)
    return response
