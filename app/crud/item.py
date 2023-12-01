from sqlalchemy.orm.session import Session
from app.db_models import models
from app.schemas.item_schemas import BaseItem


class CrudItem:

    def get_lists(self, db: Session):
        return db.query(models.Item).all()

    def create_item(self, db: Session, data: BaseItem):
        new_item = models.Item(**data.dict())
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item

    def get_item_by_id(self, id: str, db: Session):
        return db.query(models.Item).filter(models.Item.id == id).first()

    def update_item_by_id(self, id: str, data: BaseItem, db: Session):
        item_query = db.query(models.Item).filter(models.Item.id == id)
        item = item_query.first()
        if item is None:
            return
        item_query.update(data.dict(), synchronize_session=False)
        db.commit()
        return item_query.first()

    def delete_item(self, id: str, db: Session):
        item_query = db.query(models.Item).filter(models.Item.id == id)
        item = item_query.first()
        if item is None:
            return False
        item_query.delete(synchronize_session=False)
        db.commit()
        return True
