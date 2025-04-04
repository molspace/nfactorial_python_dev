from fastapi import FastAPI
from app.database.database import Base, engine
from app.api import auth, listings, comments

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(listings.router)
app.include_router(comments.router)
