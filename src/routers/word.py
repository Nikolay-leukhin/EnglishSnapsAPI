from fastapi import APIRouter

from src.database import query_get_theme_words, query_add_word
from src.schemas.word import WordModel

router = APIRouter()


@router.post('/words')
async def add_new_word(word: WordModel):
    resp = query_add_word(word)
    if isinstance(resp, Exception):
        return {
            'code': 500,
            'message': 'Something went wrong!(',
            'exception': resp
        }

    return {
        'code': 200,
        'message': 'Add word: SUCCESS',
        'word': resp.__dict__
    }


@router.get('/users/{user_id}/words')
async def get_users_word():
    ...



