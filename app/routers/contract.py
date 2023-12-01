from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm.session import Session
from app.utils.logger import log
from ..auth import oauth2
from ..db_models.database import get_db
from ..schemas.contract_schemas import ListOfContractOut, BaseContract, ContractOut
from app.controller.contract import Controller

router = APIRouter(
    prefix='/contracts',
    tags=['Contract']

)

controller = Controller()


@router.get('/', response_model=ListOfContractOut)
def get_lists(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    return controller.get_contracts_list(db=db)


@router.post("/", response_model=ContractOut)
def create_contract(create_contract: BaseContract, db: Session = Depends(get_db),
                    current_user: int = Depends(oauth2.get_current_user)):
    return controller.create_contract(db=db, data=create_contract)


@router.get("/{id}", response_model=ContractOut)
def get_contract_by_id(id: str, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    data = controller.get_contract_by_id(id=id, db=db)
    if data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"contract with id {id} not found"
        )
    return data


@router.put("/{id}", response_model=ContractOut)
def update_contract_by_id(id: str, updated_data: BaseContract, db: Session = Depends(get_db),
                          current_user: int = Depends(oauth2.get_current_user)):
    data = controller.update_contract_by_id(id=id, data=updated_data, db=db)
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"contract with id {id} not found")
    return data


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contract(id: str, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    data = controller.delete_contract(id=id, db=db)
    if data is False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"contract with id {id} not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
