from datetime import datetime

from pydantic import BaseModel
from typing import Optional

class Registration(BaseModel):
    id: str
    user_id: str
    event_id: str
    registration_date: datetime
    attended: bool = False

class CreateRegistration(BaseModel):
    user_id: str
    event_id: str
    registration_date: datetime
    attended: bool = False

class AttendedEvent(BaseModel):
    attended: bool

class UpdateRegistration(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    registration_date: datetime

class Registrations(BaseModel):
    registrations: list[Registration]

class Response(BaseModel):
    message: Optional[str] = None
    has_error: bool = False
    error_message: Optional[str] = None
    data: Optional[Registration | Registrations] = None