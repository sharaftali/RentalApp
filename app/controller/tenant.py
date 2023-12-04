from sqlalchemy.orm.session import Session
from app.schemas.tenant_schemas import ListOfTenantOut, BaseTenant, TenantOut
from app.crud.tenant import CrudTenant
from app.utils.logger import log


class Tenant:
    def __init__(self):
        self.crud = CrudTenant()

    def get_tenants_list(self, db: Session) -> ListOfTenantOut:
        return ListOfTenantOut(tenants_in_out=self.crud.get_tenants_list(db=db))

    def create_tenant(self, db: Session, data: BaseTenant) -> TenantOut:
        new_data = self.crud.create_tenant(db=db, data=data)
        return TenantOut(**new_data.__dict__)

    def get_tenant_by_id(self, id: str, db: Session) -> TenantOut or None:
        new_data = self.crud.get_tenant_by_id(db=db, id=id)
        log.debug(f"tenant with id {new_data.__dict__}")
        if new_data is None:
            return
        return TenantOut(**new_data.__dict__)

    def update_tenant_by_id(self, id: str, data: BaseTenant, db: Session) -> TenantOut or None:
        new_data = self.crud.update_tenant_by_id(db=db, id=id, data=data)
        if new_data is None:
            return
        return TenantOut(**new_data.__dict__)

    def delete_tenant(self, id: str, db: Session) -> bool:
        return bool(_ := self.crud.delete_tenant(db=db, id=id))
