from pydantic import BaseModel, EmailStr, UUID4
from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic.types import conint


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: UUID4

    created_at: datetime
    owner_id: int

    class Config:
        orm_mode = True


class UserOut(BaseModel):
    id: UUID4
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class PostOut(BaseModel):
    id: UUID4
    title: str
    content: str
    owner: UserOut

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class UserID(BaseModel):
    id: UUID4

    class Config:
        orm_mode = True
