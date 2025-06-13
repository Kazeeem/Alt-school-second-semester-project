from schemas.user import User
from schemas.event import Event
from schemas.speaker import Speaker
from schemas.registration import Registration

users: dict[str, User] = {}
events: dict[str, Event] = {}
speakers: dict[str, Speaker] = {}
registration: dict[str, Registration] = {}