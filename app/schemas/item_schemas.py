from pydantic import BaseModel, EmailStr, UUID4
from enum import Enum
from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic.types import conint

from app.schemas.schemas import UserOut


class ItemStatus(str, Enum):
    AVAILABLE = "available"
    OCCUPIED = "occupied"


class BaseItem(BaseModel):
    name: str
    rate: float
    status: ItemStatus


class ItemOut(BaseItem):
    id: UUID4
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class ListOfItemOut(BaseModel):
    items: List[ItemOut]

    class Config:
        orm_mode = True
