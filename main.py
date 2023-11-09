from fastapi import FastAPI
from apps.user.router import router as user_router
from apps.blog.router import router as blog_router

app = FastAPI()
app.include_router(user_router, prefix='/api/v1/users', tags=['Users'])
app.include_router(blog_router, prefix='/api/v1/blog', tags=['Blogs'])
