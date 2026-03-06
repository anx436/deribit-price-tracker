from app.crud.price import PriceCRUD

def test_create_price(test_db):
    crud = PriceCRUD()
    crud.create(test_db, "BTC_USD", 91234.56, 1741280000)
    
    latest = crud.get_latest_by_ticker(test_db, "BTC_USD")
    assert latest is not None
    assert latest.ticker == "BTC_USD"
    assert latest.price == 91234.56
    assert latest.timestamp == 1741280000

def test_get_all_by_ticker(test_db):
    crud = PriceCRUD()
    crud.create(test_db, "ETH_USD", 3200.0, 1741280000)
    crud.create(test_db, "ETH_USD", 3250.0, 1741281000)
    
    prices = crud.get_all_by_ticker(test_db, "ETH_USD")
    assert len(prices) == 2

def test_get_filtered_range(test_db):
    crud = PriceCRUD()
    crud.create(test_db, "BTC_USD", 90000, 1741280000)
    crud.create(test_db, "BTC_USD", 95000, 1741283600)
    
    filtered = crud.get_by_ticker_range(test_db, "BTC_USD", start=1741281000)
    assert len(filtered) == 1
    assert filtered[0].price == 95000
