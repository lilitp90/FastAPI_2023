from sqlalchemy.orm import Session
from .models import UserModel
from .schema import UserCreateSchema
from .password_utils import PasswordHasher
from ..blog.model import Blog


def get_user_by_email_id(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()


def create_new_user(db: Session, req: UserCreateSchema):
    hashed_password = PasswordHasher.hash_password(req.pasword)
    new_user = UserModel(
        first_name=req.first_name,
        last_name=req.last_name,
        email=req.email,
        password=hashed_password,
        phone_number=req.phone_number
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_id(user_id: int, db: Session):
    return db.query(UserModel).get(user_id)
