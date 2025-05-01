import uuid
from enum import StrEnum

from pydantic import BaseModel, Field

class EventActionStatus(StrEnum):
    TO_DISPATCH = 'TO_DISPATCH'
    DISPATCHED = 'DISPATCHED'
    ERROR = 'ERROR'

class EventActionDataImage(BaseModel):
    id: uuid.UUID
    subject: str
    status: EventActionStatus = EventActionStatus.TO_DISPATCH,
    reason: str = None
    s3Key: str
    deduplicationId: str
    messageGroupId: str
    headers: dict
    topic: str
    createdAt: str
    lastUpdatedAt: str

class EventAction(BaseModel):
    id: str
    operation: str
    current: EventActionDataImage = None
    previous: EventActionDataImage = None