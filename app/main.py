from fastapi import FastAPI, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
import os

from app.core.database import Base, engine, get_db
from app.crud.price import PriceCRUD
from app.schemas.price import PriceResponse
from app.routers.prices import router as prices_router

# Create tables on startup
# Base.metadata.create_all(bind=engine)

# Create tables on startup (skip in tests)
if os.getenv("TESTING") != "true":
    Base.metadata.create_all(bind=engine)

app = FastAPI(title="Deribit Price Tracker")

app.include_router(prices_router)


@app.get("/")
def root():
    return {"message": "Deribit Price Tracker API is running"}
