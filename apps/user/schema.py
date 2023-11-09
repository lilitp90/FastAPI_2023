from pydantic import BaseModel, EmailStr
from apps.blog.model import Blog


class UserCreateSchema(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    email: EmailStr
    pasword: str


class UserCreateModel(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    email: EmailStr
    blogs: list

    class Config:
        orm_mode = True


class LoginSchema(BaseModel):
    email: EmailStr
    password: str

