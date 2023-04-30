from pydantic import BaseModel


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
