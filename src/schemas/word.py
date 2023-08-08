from pydantic import BaseModel


class AddWordModel(BaseModel):
    name: str
    explanation: str
    translation: str
    transcription: str
    theme_id: int

    def __repr__(self):
        return f"Word({self.name}, {self.theme_id}"

