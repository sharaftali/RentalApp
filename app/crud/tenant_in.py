from sqlalchemy.orm.session import Session
from app.db_models import models
from app.schemas.tenant_in_out_schemas import BaseTenantInOut


class CrudTenantIn:

    def get_tenants_in_list(self, db: Session):
        return db.query(models.TenantIn).all()

    def create_tenant_in(self, db: Session, data: BaseTenantInOut):
        new_tenant_in = models.TenantIn(**data.dict())
        db.add(new_tenant_in)
        db.commit()
        db.refresh(new_tenant_in)
        return new_tenant_in

    def get_tenant_in_by_id(self, id: str, db: Session):
        return db.query(models.TenantIn).filter(models.TenantIn.id == id).first()

    def update_tenant_in_by_id(self, id: str, data: BaseTenantInOut, db: Session):
        tenant_in_query = db.query(models.TenantIn).filter(models.TenantIn.id == id)
        tenant_in = tenant_in_query.first()
        if tenant_in is None:
            return
        tenant_in_query.update(data.dict(), synchronize_session=False)
        db.commit()
        return tenant_in_query.first()

    def delete_tenant_in(self, id: str, db: Session):
        tenant_in_query = db.query(models.TenantIn).filter(models.TenantIn.id == id)
        tenant_in = tenant_in_query.first()
        if tenant_in is None:
            return False
        tenant_in_query.delete(synchronize_session=False)
        db.commit()
        return True
