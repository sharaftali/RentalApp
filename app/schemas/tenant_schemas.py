from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import List, Optional


class BaseTenant(BaseModel):
    first_name: str
    last_name: str
    email: str
    address_1: str
    address_2: Optional[str]
    phone_1: str
    phone_2: Optional[str]
    CNIC: str


class TenantOut(BaseTenant):
    id: UUID4
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class ListOfTenantOut(BaseModel):
    tenants_in_out: List[TenantOut]

    class Config:
        orm_mode = True
