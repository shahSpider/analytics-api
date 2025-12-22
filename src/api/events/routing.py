from fastapi import APIRouter
from .schema import (EventSchema, 
    EventCreateSchema,
    EventUpdateSchema, 
    EventListSchema
)

router = APIRouter()

@router.get("/")
def read_events() -> EventListSchema:
    # a bunch of items in a table
    return {
        "items": [
            {"id": 1}, {"id": 2}, {"id": 3}
        ],
        "count": 3 
    }

@router.post("/")
def create_event(payload:EventCreateSchema) -> EventSchema:
    print(payload)
    return {"id": 123}


@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    # a single row
    return {"id": event_id}

@router.put("/{event_id}")
def update_event(event_id: int, payload: EventUpdateSchema) -> EventSchema:
    # a single row
    print(payload)
    return {"id": event_id}