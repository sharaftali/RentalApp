from ..auth import oauth2
from .. import utils
from ..db_models import models as db_models
from fastapi import status, HTTPException


def login(db, user_credentials):
    user = db.query(db_models.User).filter(
        db_models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials"
        )

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials"
        )

    return oauth2.create_access_token(data={"user_id": str(user.id)})
