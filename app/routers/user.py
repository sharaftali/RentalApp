from typing import List
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from ..controller.user import User
from ..db_models import models as db_models
from ..db_models.database import get_db
from ..schemas import schemas

router = APIRouter(
    prefix="/users",
    tags=['Users']
)


user_obj = User()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return user_obj.create_user(db=db, user=user)


@router.get('/{id}', response_model=schemas.UserOut)
def get_user(UserID: schemas.UserID, db: Session = Depends(get_db), ):
    if user := user_obj.get_user(db=db, user=UserID):
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")


@router.get('/', response_model=List[schemas.UserOut])
def get_user_all(db: Session = Depends(get_db)):
    if user := user_obj.get_user_all(db=db):
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=" no user for now")
