from fastapi.testclient import TestClient
from app.main import app
from app.core.database import get_db
from app.crud.price import PriceCRUD
import pytest

def test_get_latest_price(client, test_db):
    PriceCRUD().create(test_db, "BTC_USD", 98765.43, 1741284000)
    
    response = client.get("/prices/latest?ticker=BTC_USD")
    assert response.status_code == 200
    data = response.json()
    assert data["ticker"] == "BTC_USD"
    assert data["price"] == 98765.43

def test_get_all_prices(client, test_db):
    crud = PriceCRUD()
    crud.create(test_db, "ETH_USD", 3100, 1741280000)
    crud.create(test_db, "ETH_USD", 3200, 1741281000)
    
    response = client.get("/prices/all?ticker=ETH_USD")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2

def test_get_filtered_prices(client, test_db):
    crud = PriceCRUD()
    crud.create(test_db, "BTC_USD", 90000, 1741280000)
    crud.create(test_db, "BTC_USD", 95000, 1741287200)
    
    response = client.get("/prices/filter?ticker=BTC_USD&start=1741285000")
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_missing_ticker_returns_404(client, test_db):
    crud = PriceCRUD()
    crud.create(test_db, "BTC_USD", 90000, 1741280000)
    response = client.get("/prices/latest?ticker=UNKNOWN")
    assert response.status_code == 404
