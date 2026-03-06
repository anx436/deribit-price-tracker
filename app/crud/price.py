from sqlalchemy.orm import Session
from typing import Optional, List
from app.models.price import Price

class PriceCRUD:
    def create(self, db: Session, ticker: str, price: float, timestamp: int):
        db_price = Price(ticker=ticker, price=price, timestamp=timestamp)
        db.add(db_price)
        db.commit()
        db.refresh(db_price)
        return db_price

    def get_all_by_ticker(self, db: Session, ticker: str) -> List[Price]:
        return db.query(Price).filter(Price.ticker == ticker).all()

    def get_latest_by_ticker(self, db: Session, ticker: str):
        return db.query(Price).filter(Price.ticker == ticker)\
                  .order_by(Price.timestamp.desc()).first()

    def get_by_ticker_range(self, db: Session, ticker: str,
                            start: Optional[int] = None,
                            end: Optional[int] = None) -> List[Price]:
        query = db.query(Price).filter(Price.ticker == ticker)
        if start is not None:
            query = query.filter(Price.timestamp >= start)
        if end is not None:
            query = query.filter(Price.timestamp <= end)
        return query.order_by(Price.timestamp).all()
