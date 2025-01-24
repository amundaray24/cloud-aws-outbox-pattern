import uuid
from enum import StrEnum
from datetime import datetime
from typing import Annotated, Optional

from pydantic import BaseModel, Field

class EventActionStatus(StrEnum):
    TO_DISPATCH = 'TO_DISPATCH'
    DISPATCHED = 'DISPATCHED'

class EventActionDataImage(BaseModel):
    id: uuid.UUID
    subject: str
    status: EventActionStatus = EventActionStatus.TO_DISPATCH
    s3Key: Annotated[str, Field(alias="s3_key")]
    deduplicationId: Annotated[str, Field(alias="deduplication_id")]
    messageGroupId: Annotated[str, Field(alias="message_group_id")]
    headers: dict
    topic: str
    createdAt: Annotated[datetime, Field(alias="created_at")]
    lastUpdatedAt: Annotated[datetime, Field(alias="last_updated_at")]

class EventAction(BaseModel):
    id: str
    operation: str
    current: EventActionDataImage = None
    previous: EventActionDataImage = None