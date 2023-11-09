from core.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import relationship

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(10), nullable=False)
    last_name = Column(String(10), nullable=False)
    email = Column(EmailType(128), nullable=False, unique=True)
    password = Column(String, nullable=False)
    phone_number = Column(String(20), nullable=True)
    blogs = relationship("Blog", backref='users')

