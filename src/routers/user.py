from fastapi import APIRouter
from ..schemas.user import ModelAddUser
from src.database import query_add_user


router = APIRouter()


@router.post('/user/add_user')
async def request_add_user(request: ModelAddUser):
    query_add_user(**request.__dict__)
    return {
        'code': 228,
        'message': 'idk but no exceptions'
    }
