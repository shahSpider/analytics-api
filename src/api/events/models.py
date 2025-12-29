from typing import List, Optional
from sqlmodel import SQLModel, Field


class EventModel(SQLModel, table=True):
    __tablename__ = "event"
    id: Optional[int] = Field(default=None, primary_key=True)
    page: Optional[str] = ""
    description: Optional[str] = ""


class EventListSchema(SQLModel):
    items: List[EventModel]
    count: int


class EventCreateSchema(SQLModel):
    page: str
    description: Optional[str] = Field(default="")



class EventUpdateSchema(SQLModel):
    description: str


