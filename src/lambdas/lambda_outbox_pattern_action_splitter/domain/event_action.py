from pydantic import BaseModel

class EventAction(BaseModel):
    operation: str
    data: dict