from sqlalchemy.orm.session import Session
from app.schemas.tenant_in_out_schemas import ListOfTenantOutInOut, BaseTenantInOut, TenantOutInOut
from app.crud.tenant_out import CrudTenantOut
from app.utils.logger import log


class TenantOut:
    def __init__(self):
        self.crud = CrudTenantOut()

    def get_tenants_out_list(self, db: Session) -> ListOfTenantOutInOut:
        return ListOfTenantOutInOut(tenants_in_out=self.crud.get_tenants_out_list(db=db))

    def create_tenant_out(self, db: Session, data: BaseTenantInOut) -> TenantOutInOut:
        new_data = self.crud.create_tenant_out(db=db, data=data)
        return TenantOutInOut(**new_data.__dict__)

    def get_tenant_out_by_id(self, id: str, db: Session) -> TenantOutInOut or None:
        new_data = self.crud.get_tenant_out_by_id(db=db, id=id)
        log.debug(f"tenant_out with id {new_data.__dict__}")
        if new_data is None:
            return
        return TenantOutInOut(**new_data.__dict__)

    def update_tenant_out_by_id(self, id: str, data: BaseTenantInOut, db: Session) -> TenantOutInOut or None:
        new_data = self.crud.update_tenant_out_by_id(db=db, id=id, data=data)
        if new_data is None:
            return
        return TenantOutInOut(**new_data.__dict__)

    def delete_tenant_out(self, id: str, db: Session) -> bool:
        return bool(_ := self.crud.delete_tenant_out(db=db, id=id))
