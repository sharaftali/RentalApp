from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import List, Optional, Any


class ItemDetails(BaseModel):
    lights_qty: Optional[int] = 0


class BaseTenantInOut(BaseModel):
    contract_id: UUID4
    details: ItemDetails


class TenantOutInOut(BaseTenantInOut):
    id: UUID4
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class ListOfTenantOutInOut(BaseModel):
    tenants_in_out: List[TenantOutInOut]

    class Config:
        orm_mode = True
