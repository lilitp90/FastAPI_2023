from fastapi_jwt_auth import AuthJWT
from fastapi import Header
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi import Depends, HTTPException, status
from .service import get_user_by_id
from sqlalchemy.orm import Session
from core.deps import get_db


def get_current_user(db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    try:
        authorize.jwt_required()
    except AuthJWTException as e:
        print(getattr(e, 'message', e), 'errrror')
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Unautorized")
    user_id = authorize.get_jwt_subject()
    user = get_user_by_id(user_id, db)

    return user
