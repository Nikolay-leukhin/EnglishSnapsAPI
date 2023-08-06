from pydantic import BaseModel


class ThemeModel(BaseModel):
    theme_name: str
