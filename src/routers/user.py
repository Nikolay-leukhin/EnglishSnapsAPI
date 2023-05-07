from fastapi import APIRouter
from ..schemas.user import ModelAddUser
from ..database import query_add_user, query_is_user_exist


router = APIRouter()


@router.post('/user/add_user')
async def request_add_user(request: ModelAddUser):
    added_user = query_add_user(**request.__dict__)
    return {
        'code': 200,
        'message': 'User has been added',
        'added_user': added_user
    }


@router.post('/user/is_exist')
async def is_user_exist(email: str, password: str):
    """returns bool type: does user exist or not?"""
    user_exists = query_is_user_exist(email=email, password=password)
    return {
        'code': 200,
        'content': user_exists
    }