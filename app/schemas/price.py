from pydantic import BaseModel

class PriceResponse(BaseModel):
    id: int
    ticker: str
    price: float
    timestamp: int

    class Config:
        from_attributes = True
