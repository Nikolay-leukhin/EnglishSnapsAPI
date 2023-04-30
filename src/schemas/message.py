from pydantic import BaseModel


class ModelMessageSend(BaseModel):
    user_id: int
    session_id: int
    message_order: int
    message_text: str
    is_bot: bool = False
