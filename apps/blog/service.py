from sqlalchemy.orm import Session
from .model import Blog
from .schema import BlogAddSchema
from fastapi import HTTPException, status


def get_all(db: Session):
    blogs = db.query(Blog).all()
    return blogs


def create_new_blog(data: BlogAddSchema, db: Session):
    new_blog = Blog(title=data.title, body=data.body, user_id=2)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete_blogs(id: int, db: Session):
    blog = db.query(Blog).get(id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} does not exist')
    db.delete(blog)
    db.commit()
