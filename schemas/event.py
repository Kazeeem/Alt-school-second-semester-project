from datetime import datetime

from pydantic import BaseModel
from typing import Optional

class Event(BaseModel):
    id: str
    title: str
    location: str
    date: datetime
    is_open: bool = True

class CreateEvent(BaseModel):
    title: str
    location: str
    date: datetime
    is_open: bool = True

class UpdateEvent(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

class CloseEvent(BaseModel):
    is_open: bool

class Events(BaseModel):
    events: list[Event]

class Response(BaseModel):
    message: Optional[str] = None
    has_error: bool = False
    error_message: Optional[str] = None
    data: Optional[Event | Events] = None