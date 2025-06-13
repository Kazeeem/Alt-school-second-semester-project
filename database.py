from uuid import uuid4

from schemas.user import User
from schemas.event import Event
from schemas.speaker import Speaker
from schemas.registration import Registration

users: dict[str, User] = {}
events: dict[str, Event] = {}
speakers: dict[str, Speaker] = {}
registration: dict[str, Registration] = {}

speakers_data = [
    {"name": "Kazeem Asifat", "topic": "Using Python To Build Aircraft Console"},
    {"name": "Taylor Ortwell", "topic": "PHP & Python in Synchronicity"},
    {"name": "Nuno Maduro", "topic": "Evolution of Python for Asynchronous Actions"},
]

for data in speakers_data:
    speaker = Speaker(id=str(uuid4()), **data)
    speakers[speaker.id] = speaker