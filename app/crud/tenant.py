from sqlalchemy.orm.session import Session
from app.db_models import models
from app.schemas.tenant_schemas import BaseTenant


class CrudTenant:

    def get_tenants_list(self, db: Session):
        return db.query(models.Tenant).all()

    def create_tenant(self, db: Session, data: BaseTenant):
        new_tenant = models.Tenant(**data.dict())
        db.add(new_tenant)
        db.commit()
        db.refresh(new_tenant)
        return new_tenant

    def get_tenant_by_id(self, id: str, db: Session):
        return db.query(models.Tenant).filter(models.Tenant.id == id).first()

    def update_tenant_by_id(self, id: str, data: BaseTenant, db: Session):
        tenant_query = db.query(models.Tenant).filter(models.Tenant.id == id)
        tenant = tenant_query.first()
        if tenant is None:
            return
        tenant_query.update(data.dict(), synchronize_session=False)
        db.commit()
        return tenant_query.first()

    def delete_tenant(self, id: str, db: Session):
        tenant_query = db.query(models.Tenant).filter(models.Tenant.id == id)
        tenant = tenant_query.first()
        if tenant is None:
            return False
        tenant_query.delete(synchronize_session=False)
        db.commit()
        return True
