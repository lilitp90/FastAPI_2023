from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from core.deps import get_db
from .model import Blog
from .schema import BlogResponseSchema, BlogAddSchema
from .service import get_all, create_new_blog, delete_blogs

router = APIRouter()


@router.get('', response_model=List[BlogResponseSchema])
def get_all_blogs(db: Session = Depends(get_db)):
    return get_all(db)


@router.post('', status_code=status.HTTP_201_CREATED)
def create_blog(request: BlogAddSchema, db: Session = Depends(get_db)):
    return create_new_blog(data=request, db=db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    delete_blogs(id=id, db=db)


@router.put("/{blog_id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(blog_id: int, req: BlogAddSchema, db: Session = Depends(get_db)):
    blog = db.query(Blog).get(blog_id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {blog_id} does not exist')

    blog.title = req.title
    db.commit()
    return {'detail': 'updated'}


@router.get('/{blog_id}', response_model=BlogResponseSchema)
def get_blog_by_id(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    # blog = db.query(Blog).join
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {blog_id} does not exist')
    return blog