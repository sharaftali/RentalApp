from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm.session import Session

from ..auth import oauth2
from ..db_models.database import get_db
from ..db_models import models
from ..schemas import schemas
from ..schemas.item_schemas import ListOfItemOut, BaseItem, ItemOut
from app.controller.item import Item

router = APIRouter(
    prefix='/items',
    tags=['Item']

)

item = Item()


@router.get('/', response_model=ListOfItemOut)
def get_lists(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    return item.get_item_lists(db=db)


@router.post("/", response_model=ItemOut)
def create_item(create_item: BaseItem, db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    return item.create_item(db=db, data=create_item)


@router.get("/{id}", response_model=ItemOut)
def get_item_by_id(id: str, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    data = item.get_item_by_id(id=id, db=db)
    if data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"item with id {id} not found"
        )
    return data


@router.put("/{id}", response_model=ItemOut)
def update_item_by_id(id: str, updated_data: BaseItem, db: Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)):
    data = item.update_item_by_id(id=id, data=updated_data, db=db)
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with id {id} not found")
    return data


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(id: str, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    data = item.delete_item(id=id, db=db)
    if data is False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item with id {id} not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
