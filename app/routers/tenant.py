from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm.session import Session
from app.utils.logger import log
from ..auth import oauth2
from ..db_models.database import get_db
from ..schemas.tenant_schemas import ListOfTenantOut, BaseTenant, TenantOut
from app.controller.tenant import Tenant

router = APIRouter(
    prefix='/tenants',
    tags=['Tenant']

)

tenant = Tenant()


@router.get('/', response_model=ListOfTenantOut)
def get_tenants_list(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    return tenant.get_tenants_list(db=db)


@router.post("/", response_model=TenantOut)
def create_tenant(create_tenant_in: BaseTenant, db: Session = Depends(get_db),
                     current_user: int = Depends(oauth2.get_current_user)):
    return tenant.create_tenant(db=db, data=create_tenant_in)


@router.get("/{id}", response_model=TenantOut)
def get_tenant_by_id(id: str, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    data = tenant.get_tenant_by_id(id=id, db=db)
    if data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"tenant_in with id {id} not found"
        )
    return data


@router.put("/{id}", response_model=TenantOut)
def update_tenant_by_id(id: str, updated_data: BaseTenant, db: Session = Depends(get_db),
                           current_user: int = Depends(oauth2.get_current_user)):
    data = tenant.update_tenant_by_id(id=id, data=updated_data, db=db)
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"tenant_in with id {id} not found")
    return data


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tenant(id: str, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    data = tenant.delete_tenant(id=id, db=db)
    if data is False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"tenant_in with id {id} not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
