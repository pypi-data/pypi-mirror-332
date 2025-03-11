from datetime import datetime
from typing import Optional

from pydantic import UUID4, BaseModel


class BackupCreate(BaseModel):
    kb_id: UUID4


class BackupCreateResponse(BaseModel):
    id: UUID4


class KBDataResponse(BaseModel):
    id: UUID4
    slug: str
    title: str
    created: datetime


class BackupResponse(BaseModel):
    id: UUID4
    account_id: UUID4
    started_at: datetime
    kb_data: KBDataResponse
    finished_at: Optional[datetime]
    size: Optional[int]


class BackupRestore(BaseModel):
    slug: str
