from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..controller.auth import login
from ..db_models import database
from ..schemas import schemas

router = APIRouter(tags=['Authentication'])


@router.post('/login', response_model=schemas.Token)
def login_(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    access_token = login(db=db, user_credentials=user_credentials)

    return {"access_token": access_token, "token_type": "bearer"}
