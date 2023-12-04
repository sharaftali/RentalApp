from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm.session import Session
from app.utils.logger import log
from ..auth import oauth2
from ..db_models.database import get_db
from ..schemas.tenant_in_out_schemas import ListOfTenantOutInOut, BaseTenantInOut, TenantOutInOut
from app.controller.tenant_in import TenantIn

router = APIRouter(
    prefix='/tenants_in',
    tags=['Tenant_in']

)

tenant = TenantIn()


@router.get('/', response_model=ListOfTenantOutInOut)
def get_tenants_in_list(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    return tenant.get_tenants_in_list(db=db)


@router.post("/", response_model=TenantOutInOut)
def create_tenant_in(create_tenant_in: BaseTenantInOut, db: Session = Depends(get_db),
                     current_user: int = Depends(oauth2.get_current_user)):
    return tenant.create_tenant_in(db=db, data=create_tenant_in)


@router.get("/{id}", response_model=TenantOutInOut)
def get_tenant_in_by_id(id: str, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    data = tenant.get_tenant_in_by_id(id=id, db=db)
    if data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"tenant_in with id {id} not found"
        )
    return data


@router.put("/{id}", response_model=TenantOutInOut)
def update_tenant_in_by_id(id: str, updated_data: BaseTenantInOut, db: Session = Depends(get_db),
                           current_user: int = Depends(oauth2.get_current_user)):
    data = tenant.update_tenant_in_by_id(id=id, data=updated_data, db=db)
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"tenant_in with id {id} not found")
    return data


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tenant_in(id: str, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    data = tenant.delete_tenant_in(id=id, db=db)
    if data is False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"tenant_in with id {id} not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
