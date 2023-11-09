from core.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship



class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(10))
    body = Column(String(20))
    user_id = Column(Integer(), ForeignKey("users.id"))
    # blogs = relationship("UserModel", backref='blogs')

