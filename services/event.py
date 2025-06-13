from uuid import UUID, uuid4
from fastapi import HTTPException

from database import events
from schemas.event import Event, CreateEvent, UpdateEvent


class EventService:

    @staticmethod
    def get_all_events():
        return list(events.values())

    @staticmethod
    def get_event_by_id(event_id):
        event = events.get(str(event_id))

        if not event:
            return None
        return event

    @staticmethod
    def create_event(event_data: CreateEvent):
        event = Event(id=str(uuid4()), **event_data.model_dump())
        events[event.id] = event
        return event

    @staticmethod
    def update_event(event_id: UUID, event_data: UpdateEvent):
        event = events.get(str(event_id))
        if not event:
            return None

        event.title = event_data.title
        event.location = event_data.location
        event.date = event_data.date
        return event

    @staticmethod
    def delete_event(event_id: UUID):
        event = events.get(str(event_id))
        if not event:
            return None

        del events[event.id]
        return True

    @staticmethod
    def close_event(event_id: UUID):
        event = events.get(str(event_id))
        if not event:
            return None

        event.is_open = False
        return event


event_service = EventService()