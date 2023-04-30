from datetime import datetime

from pydantic import BaseModel


class ModelSessionSend(BaseModel):
    session_name: str
    created_at: datetime
