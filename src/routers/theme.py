from fastapi import APIRouter

from src.database import query_get_theme_words
from src.schemas.word import WordModel

router = APIRouter()


@router.post('/themes')
async def add_theme():
    ...


@router.get('/users/{id}/themes ')
async def get_users_themes():
    ...


@router.get('/themes/{theme_id}/words')
async def get_theme_words(theme_id: int):
    words: list[WordModel] = query_get_theme_words(theme_id)
    words_kv = [item.__dict__ for item in words]
    return words_kv