from sqlalchemy.orm.session import Session
from app.schemas.contract_schemas import ListOfContractOut, BaseContract, ContractOut
from app.crud.contract import CrudContract
from app.utils.logger import log


class Controller:
    def __init__(self):
        self.crud = CrudContract()

    def get_contracts_list(self, db: Session) -> ListOfContractOut:
        return ListOfContractOut(contracts=self.crud.get_contracts_list(db=db))

    def create_contract(self, db: Session, data: BaseContract) -> ContractOut:
        new_data = self.crud.create_contract(db=db, data=data)
        log.debug(f"contract created {new_data.__dict__}")
        return ContractOut(**new_data.__dict__)

    def get_contract_by_id(self, id: str, db: Session):
        new_data = self.crud.get_contract_by_id(db=db, id=id)
        if new_data is None:
            return
        log.debug(f"Item with id {new_data.__dict__}")
        return ContractOut(**new_data.__dict__)

    def update_contract_by_id(self, id: str, data: BaseContract, db: Session):
        new_data = self.crud.update_contract_by_id(db=db, id=id, data=data)
        if new_data is None:
            return
        return ContractOut(**new_data.__dict__)

    def delete_contract(self, id: str, db: Session):
        return bool(_ := self.crud.delete_contract(db=db, id=id))
