from fastapi import APIRouter, Depends
from sqlmodel import Session
 
from src.api.db.session import get_session

from .models import (
    EventModel, 
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


@router.post("/", response_model=EventModel)
def create_event(payload:EventCreateSchema, session: Session = Depends(get_session)) -> EventModel:
    data = payload.model_dump()
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)

    return {"id": 123, **data}


@router.get("/{event_id}")
def get_event(event_id: int) -> EventModel:
    # a single row
    return {"id": event_id}


@router.put("/{event_id}")
def update_event(event_id: int, payload: EventUpdateSchema) -> EventModel:
    # a single row
    data = payload.model_dump()
    return {"id": event_id, **data}