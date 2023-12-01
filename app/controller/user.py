from typing import List

from .. import utils
from ..schemas import schemas
from ..db_models import models as db_models


class User:

    def create_user(self, db, user: schemas.UserCreate) -> schemas.UserOut:
        # hash the password - user.password
        hashed_password = utils.hash(user.password)
        user.password = hashed_password

        new_user = db_models.User(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def get_user(self, db, user: schemas.UserID) -> schemas.UserOut:
        return db.query(db_models.User).filter(db_models.User.id == user.id).first()

    def get_user_all(self, db) -> List[schemas.UserOut]:
        return db.query(db_models.User).all()
