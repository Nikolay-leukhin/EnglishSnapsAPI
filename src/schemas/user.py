from pydantic import BaseModel


# messages models
class ModelMessageSend(BaseModel):
    user_id: int
    session_id: int
    message_order: int
    message_text: str
    is_bot: bool


# user models
class ModelAddUser(BaseModel):
    nickname: str
    password: str
    avatar_path: str = None
    email: str
    phone: str
    vk_contact: str = None
    tg_contact: str = None
    longitude: str = None
    latitude: str = None
    english_level: str = None
    role: str = None
    is_active: bool = False
    is_superuser: bool = False
