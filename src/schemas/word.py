from pydantic import BaseModel


class WordModel(BaseModel):
    id: int = None
    name: str
    explanation: str
    translation: str
    transcription: str
    theme_id: int


    def __repr__(self):
        return f"Word({self.id}, {self.name}, {self.theme_id}"



