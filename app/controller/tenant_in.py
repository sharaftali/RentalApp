from sqlalchemy.orm.session import Session
from app.schemas.tenant_in_out_schemas import ListOfTenantOutInOut, BaseTenantInOut, TenantOutInOut
from app.crud.tenant_in import CrudTenantIn
from app.utils.logger import log


class TenantIn:
    def __init__(self):
        self.crud = CrudTenantIn()

    def get_tenants_in_list(self, db: Session) -> ListOfTenantOutInOut:
        return ListOfTenantOutInOut(tenants_in_out=self.crud.get_tenants_in_list(db=db))

    def create_tenant_in(self, db: Session, data: BaseTenantInOut) -> TenantOutInOut:
        new_data = self.crud.create_tenant_in(db=db, data=data)
        return TenantOutInOut(**new_data.__dict__)

    def get_tenant_in_by_id(self, id: str, db: Session) -> TenantOutInOut or None:
        new_data = self.crud.get_tenant_in_by_id(db=db, id=id)
        log.debug(f"tenant_in with id {new_data.__dict__}")
        if new_data is None:
            return
        return TenantOutInOut(**new_data.__dict__)

    def update_tenant_in_by_id(self, id: str, data: BaseTenantInOut, db: Session) -> TenantOutInOut or None:
        new_data = self.crud.update_tenant_in_by_id(db=db, id=id, data=data)
        if new_data is None:
            return
        return TenantOutInOut(**new_data.__dict__)

    def delete_tenant_in(self, id: str, db: Session) -> bool:
        return bool(_ := self.crud.delete_tenant_in(db=db, id=id))
