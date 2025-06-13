from pydantic import BaseModel
from typing import Optional

class Speaker(BaseModel):
    id: str
    name: str
    topic: str

class CreateSpeaker(BaseModel):
    name: str
    topic: str

class UpdateSpeaker(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

class Speakers(BaseModel):
    speakers: list[Speaker]

class Response(BaseModel):
    message: Optional[str] = None
    has_error: bool = False
    error_message: Optional[str] = None
    data: Optional[Speaker | Speakers] = None