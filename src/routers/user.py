from fastapi import APIRouter
from ..schemas.user import ModelAddUser
from ..database import query_add_user, query_is_user_exist


router = APIRouter()


@router.post('/user/add_user')
async def request_add_user(request: ModelAddUser):
    query_add_user(**request.__dict__)
    return {
        'code': 228,
        'message': 'idk but no exceptions'
    }


@router.get('/user/is_exist/email={email}&pwd={password}')
async def is_user_exist(email: str, password: str):
    """returns bool type: does user exist or not?"""
    user_exists = query_is_user_exist(email=email, password=password)
    return user_exists