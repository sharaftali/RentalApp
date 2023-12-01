from sqlalchemy.orm.session import Session
from app.db_models import models
from app.schemas.contract_schemas import BaseContract


class CrudContract:

    def get_contracts_list(self, db: Session):
        return db.query(models.Contract).all()

    def create_contract(self, db: Session, data: BaseContract):
        new_contract = models.Contract(**data.dict())
        db.add(new_contract)
        db.commit()
        db.refresh(new_contract)
        return new_contract

    def get_contract_by_id(self, id: str, db: Session):
        return db.query(models.Contract).filter(models.Contract.id == id).first()

    def update_contract_by_id(self, id: str, data: BaseContract, db: Session):
        contract_query = db.query(models.Contract).filter(models.Contract.id == id)
        contract = contract_query.first()
        if contract is None:
            return
        contract_query.update(data.dict(), synchronize_session=False)
        db.commit()
        return contract_query.first()

    def delete_contract(self, id: str, db: Session):
        contract_query = db.query(models.Contract).filter(models.Contract.id == id)
        contract = contract_query.first()
        if contract is None:
            return False
        contract_query.delete(synchronize_session=False)
        db.commit()
        return True
