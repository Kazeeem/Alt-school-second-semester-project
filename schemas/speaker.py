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
    topic: Optional[str] = None

class Response(BaseModel):
    success: bool = True
    message: Optional[str] = None
    data: Optional[Speaker | list[Speaker]] = None