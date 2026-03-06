from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from app.core.database import get_db
from app.crud.price import PriceCRUD
from app.schemas.price import PriceResponse

router = APIRouter(prefix="/prices", tags=["prices"])


@router.get("/all", response_model=List[PriceResponse])
def get_all_prices(ticker: str = Query(..., description="e.g. BTC_USD"),
                   db: Session = Depends(get_db)):
    prices = PriceCRUD().get_all_by_ticker(db, ticker)
    if not prices:
        raise HTTPException(status_code=404, detail="No data for this ticker")
    return prices


@router.get("/latest", response_model=PriceResponse)
def get_latest_price(ticker: str = Query(...),
                     db: Session = Depends(get_db)):
    price = PriceCRUD().get_latest_by_ticker(db, ticker)
    if not price:
        raise HTTPException(status_code=404, detail="No data for this ticker")
    return price


@router.get("/filter", response_model=List[PriceResponse])
def get_filtered_prices(
    ticker: str = Query(...),
    start: Optional[int] = Query(None, description="Start UNIX timestamp"),
    end: Optional[int] = Query(None, description="End UNIX timestamp"),
    db: Session = Depends(get_db)
):
    prices = PriceCRUD().get_by_ticker_range(db, ticker, start, end)
    if not prices:
        raise HTTPException(status_code=404, detail="No data for this ticker")
    return prices
