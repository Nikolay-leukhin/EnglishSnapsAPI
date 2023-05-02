from pydantic import BaseModel
from enum import Enum


class BotRoles(str, Enum):
    assistant = 'assistant'
    user = 'user'
    system = 'system'


class ModelMessageSend(BaseModel):
    user_id: int
    session_id: int
    message_order: int
    message_text: str
    sender: BotRoles = BotRoles.user



