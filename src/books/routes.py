from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.service import BookService
from src.books.schemas import Book, BookCreateModel, BookUpdateModel
from src.books.models import Book
from src.db.main import get_session
from typing import List
from src.auth.dependencies import AccessTokenBearer


book_router = APIRouter()
book_service = BookService()
access_token_bearer = AccessTokenBearer()


#Получение всех книг
@book_router.get('/', response_model=List[Book])
async def get_all_books(session:AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    return books


#Create
@book_router.post('/', status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_a_book(book_data: BookCreateModel, session:AsyncSession = Depends(get_session), user_details=Depends(access_token_bearer)) -> dict:
    new_book = await book_service.create_book(book_data, session)
    return new_book


#Read
@book_router.get('/{book_uid}', response_model=Book)
async def get_book(book_uid: str, session:AsyncSession = Depends(get_session), user_details=Depends(access_token_bearer)) -> dict:
    book = await book_service.get_book(book_uid, session)
    if book:
        return book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Book not found")


#Update
@book_router.patch('/{book_uid}', response_model=Book)
async def update_book(book_uid: str,  book_update_data:BookUpdateModel, session:AsyncSession = Depends(get_session), user_details=Depends(access_token_bearer)) -> dict:
    updated_book = await book_service.update_book(book_uid, book_update_data, session)
    if updated_book:
        return updated_book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not found')


#Delete
@book_router.delete('/{book_uid}', response_model=Book)
async def delete_book(book_uid: str, session:AsyncSession = Depends(get_session), user_details=Depends(access_token_bearer)):
    book_to_delete = await book_service.delete_book(book_uid, session)

    if book_to_delete:
        return None
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not found')