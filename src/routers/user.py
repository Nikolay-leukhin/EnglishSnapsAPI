from fastapi import APIRouter

router = APIRouter()


@router.post('/add_user')
def request_add_user(name: str, email: str, profession: str):
    return 'OKEY'
