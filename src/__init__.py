from fastapi import FastAPI, status
from src.books.routes import book_router
from src.auth.routes import auth_router
from src.errors import register_all_errors
from src.reviews.routes import review_router
from src.tags.routes import tags_router
from contextlib import asynccontextmanager
from src.db.main import init_db


version = 'v1'


app = FastAPI(
    title="Bookly",
    description="A REST API for a book review web service",
    version=version,
)

register_all_errors(app)

app.include_router(auth_router, prefix=f"/api/{version}/auth", tags=["auth"])
app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])
app.include_router(review_router, prefix=f"/api/{version}/reviews", tags=["reviews"])
app.include_router(tags_router, prefix=f"/api/{version}/tags", tags=["tags"])