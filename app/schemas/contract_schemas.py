from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import List, Optional


class BaseContract(BaseModel):
    item_id: UUID4
    start_date: datetime
    end_date: datetime
    terms: Optional[str]


class ContractOut(BaseContract):
    id: UUID4
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class ListOfContractOut(BaseModel):
    contracts: List[ContractOut]

    class Config:
        orm_mode = True
