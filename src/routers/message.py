from fastapi import APIRouter

from ..ai_bot.bot import BotAssistant

from ..database import query_add_message
from ..schemas.message import ModelMessageSend

router = APIRouter()


@router.post('/message/add_message')
async def add_message(request: ModelMessageSend):
    bot_response = BotAssistant(request.__dict__).make_bot_request()
    query_add_message(**request.__dict__)
    query_add_message(**bot_response)
    return bot_response
