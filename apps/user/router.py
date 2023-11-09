from typing import Annotated, Union

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi_jwt_auth.exceptions import AuthJWTException

from core.deps import get_db
from apps.core import config
from .models import UserModel
from .password_utils import PasswordHasher
from .schema import UserCreateSchema, UserCreateModel, LoginSchema
from .service import get_user_by_email_id, create_new_user, get_user_by_id
from .user_utils import get_current_user

router = APIRouter()


@router.post('', status_code=status.HTTP_201_CREATED, response_model=
             UserCreateModel)
def create_user(req: UserCreateSchema, db: Session = Depends(get_db)):
    user = get_user_by_email_id(db=db, email=req.email)
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User already exists")
    new_user = create_new_user(db=db, req=req)
    return new_user


@router.get('', response_model=UserCreateModel)
def get_user(db: Session = Depends(get_db),
            current_user: UserModel = Depends(get_current_user)):
    print(current_user, 'curr user')
    user = get_user_by_id(user_id=current_user, db=db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with ID {current_user} not found')
    return user


@router.post('/login')
def login(request: LoginSchema, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    user = get_user_by_email_id(email=request.email, db=db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with email {request.email} not found')
    valid_password = PasswordHasher.verify_password(request.password, user.password)
    if not valid_password:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Invalid password')
    print(user.email, 'emailll')
    access_token = authorize.create_access_token(subject=user.id)
    refresh_token = authorize.create_refresh_token(subject=user.id)
    return {"access_token": access_token,
            "refresh_token": refresh_token}
