from sqlalchemy.orm.session import Session
from app.schemas.item_schemas import ListOfItemOut, BaseItem, ItemOut
from app.crud.item import CrudItem


class Item:
    def __init__(self):
        self.crud = CrudItem()

    def get_item_lists(self, db: Session) -> ListOfItemOut:
        return ListOfItemOut(items=self.crud.get_lists(db=db))

    def create_item(self, db: Session, data: BaseItem) -> ItemOut:
        new_data = self.crud.create_item(db=db, data=data)
        return ItemOut(**new_data.__dict__)

    def get_item_by_id(self, id: str, db: Session):
        new_data = self.crud.get_item_by_id(db=db, id=id)
        if new_data is None:
            return
        return ItemOut(**new_data.__dict__)

    def update_item_by_id(self, id: str, data: BaseItem, db: Session):
        new_data = self.crud.update_item_by_id(db=db, id=id, data=data)
        if new_data is None:
            return
        return ItemOut(**new_data.__dict__)

    def delete_item(self, id: str, db: Session):
        return bool(_ := self.crud.delete_item(db=db, id=id))
