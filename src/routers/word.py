from fastapi import APIRouter

from src.database import query_get_theme_words
from src.schemas.word import WordModel

router = APIRouter()


@router.post('/words')
async def add_new_word():
    ...


@router.get('/users/{user_id}/words')
async def get_users_word():
    ...



