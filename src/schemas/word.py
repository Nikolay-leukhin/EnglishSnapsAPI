from pydantic import BaseModel


class WordModel(BaseModel):
    id: int
    name: str
    explanation: str
    translation: str
    transcription: str
    theme_id: int = False


    def __repr__(self):
        return f"Word({self.id}, {self.name}, {self.theme_id}"
