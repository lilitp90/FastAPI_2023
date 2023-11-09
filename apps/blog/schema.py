from pydantic import BaseModel


class BlogAddSchema(BaseModel):
    title: str
    body: str


class BlogResponseSchema(BaseModel):
    title: str

    class Config:
        orm_mode = True


class MSG(BaseModel):
    msg: str

    class Config:
        orm_mode = True
