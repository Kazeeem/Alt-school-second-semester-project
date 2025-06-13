from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: str
    name: str
    email: str
    is_active: bool = True

class UserCreate(BaseModel):
    name: str
    email: str
    is_active: bool = True

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

class UserDeactivate(BaseModel):
    is_active: bool

class Users(BaseModel):
    users: list[User]

class Response(BaseModel):
    message: Optional[str] = None
    has_error: bool = False
    error_message: Optional[str] = None
    data: Optional[User | Users] = None