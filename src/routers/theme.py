from typing import List

from fastapi import APIRouter

from src.database import query_get_theme_words, query_add_theme, query_get_themes
from src.schemas.theme import AddThemeModel
from src.schemas.word import WordModel

router = APIRouter()


@router.post('/themes')
async def add_theme(data: AddThemeModel):
    req = query_add_theme(data)
    if req is None:
        return {
            'code': 500,
            'message': 'Something went wrong!('
        }

    return {
        'code': 200,
        'message': 'Add theme: SUCCESS'
    }



@router.get('/users/{id}/themes ')
async def get_users_themes():
    ...


@router.get('/themes/{theme_id}/words')
async def get_theme_words(theme_id: int):
    words: List[WordModel] = query_get_theme_words(theme_id)
    if len(words) == 0:
        return {
            'status': 400,
            'data': []
        }
    words_kv = [item.__dict__ for item in words]
    return {
        'status': 200,
        'data': words_kv
    }


@router.get('/themes')
async def get_themes():
    themes = query_get_themes()
    if themes is None:
        return {
            'code': 500,
            'message': 'Temporary server error',
            'data': None
        }

    themes = [
        item.__dict__ for item in themes
    ]

    return {
        'code': 200,
        'message': 'GET THEMES: SUCCESS',
        'data': themes
    }
