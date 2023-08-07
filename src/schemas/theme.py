from pydantic import BaseModel


class AddThemeModel(BaseModel):
    theme_name: str


class GetThemeModel(BaseModel):
    id: int
    theme_name: str

    def __repr__(self):
        return f"GetThemeModel({self.id}, {self.theme_name})"
