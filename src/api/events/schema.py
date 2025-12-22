from typing import List, Optional
from pydantic import BaseModel

class EventCreateSchema(BaseModel):
    path: str
    page: Optional[str] = ""


class EventUpdateSchema(BaseModel):
    description  : str

class EventSchema(BaseModel):
    id: int

class EventListSchema(BaseModel):
    items: List[EventSchema]
    count: int