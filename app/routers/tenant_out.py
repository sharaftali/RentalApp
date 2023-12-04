from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm.session import Session
from app.utils.logger import log
from ..auth import oauth2
from ..db_models.database import get_db
from ..schemas.tenant_in_out_schemas import ListOfTenantOutInOut, BaseTenantInOut, TenantOutInOut
from app.controller.tenant_out import TenantOut

router = APIRouter(
    prefix='/tenants_out',
    tags=['Tenant_out']

)

tenant = TenantOut()


@router.get('/', response_model=ListOfTenantOutInOut)
def get_tenants_out_list(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    return tenant.get_tenants_out_list(db=db)


@router.post("/", response_model=TenantOutInOut)
def create_tenant_out(create_tenant_out: BaseTenantInOut, db: Session = Depends(get_db),
                     current_user: int = Depends(oauth2.get_current_user)):
    return tenant.create_tenant_out(db=db, data=create_tenant_out)


@router.get("/{id}", response_model=TenantOutInOut)
def get_tenant_out_by_id(id: str, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    data = tenant.get_tenant_out_by_id(id=id, db=db)
    if data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"tenant_out with id {id} not found"
        )
    return data


@router.put("/{id}", response_model=TenantOutInOut)
def update_tenant_out_by_id(id: str, updated_data: BaseTenantInOut, db: Session = Depends(get_db),
                           current_user: int = Depends(oauth2.get_current_user)):
    data = tenant.update_tenant_out_by_id(id=id, data=updated_data, db=db)
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"tenant_out with id {id} not found")
    return data


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tenant_out(id: str, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    data = tenant.delete_tenant_out(id=id, db=db)
    if data is False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"tenant_out with id {id} not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
