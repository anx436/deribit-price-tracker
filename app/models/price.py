from sqlalchemy import Column, Integer, String, Float, BigInteger
from app.core.database import Base

class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True, nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(BigInteger, nullable=False)  # UNIX timestamp
