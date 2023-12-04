from sqlalchemy.orm.session import Session
from app.db_models import models
from app.schemas.tenant_in_out_schemas import BaseTenantInOut


class CrudTenantOut:

    def get_tenants_out_list(self, db: Session):
        return db.query(models.TenantOut).all()

    def create_tenant_out(self, db: Session, data: BaseTenantInOut):
        new_tenant_out = models.TenantOut(**data.dict())
        db.add(new_tenant_out)
        db.commit()
        db.refresh(new_tenant_out)
        return new_tenant_out

    def get_tenant_out_by_id(self, id: str, db: Session):
        return db.query(models.TenantOut).filter(models.TenantOut.id == id).first()

    def update_tenant_out_by_id(self, id: str, data: BaseTenantInOut, db: Session):
        tenant_out_query = db.query(models.TenantOut).filter(models.TenantOut.id == id)
        tenant_out = tenant_out_query.first()
        if tenant_out is None:
            return
        tenant_out_query.update(data.dict(), synchronize_session=False)
        db.commit()
        return tenant_out_query.first()

    def delete_tenant_out(self, id: str, db: Session):
        tenant_out_query = db.query(models.TenantOut).filter(models.TenantOut.id == id)
        tenant_out = tenant_out_query.first()
        if tenant_out is None:
            return False
        tenant_out_query.delete(synchronize_session=False)
        db.commit()
        return True
