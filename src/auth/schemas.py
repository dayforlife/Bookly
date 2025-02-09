from pydantic import BaseModel, Field
from src.books.schemas import Book
from src.reviews.schemas import ReviewModel
from datetime import datetime
from typing import List
import uuid


class UserCreateModel(BaseModel):
    first_name: str = Field(max_length=25)
    last_name: str = Field(max_length=25)
    username: str = Field(max_length=50)
    email: str = Field(max_length=50)
    password: str = Field(min_length=3)

class UserModel(BaseModel):
    uid: uuid.UUID
    username: str
    email: str
    first_name: str
    last_name: str
    is_verified: bool
    password_hash: str = Field(exclude=True)
    created_at: datetime
    updated_at: datetime

class UserBooksModel(UserModel):
    books: List[Book]
    reviews: List[ReviewModel]


class UserLoginModel(BaseModel):
    email: str = Field(max_length=50)
    password: str = Field(min_length=3)