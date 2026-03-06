import asyncio
import time
from app.celery_app import celery_app
from app.clients.deribit import DeribitClient
from app.core.database import SessionLocal
from app.crud.price import PriceCRUD

@celery_app.task
def fetch_and_save_prices():
    """Fetches BTC_USD and ETH_USD every minute (called by Celery Beat)."""
    async def _fetch():
        client = DeribitClient()
        db = SessionLocal()
        crud = PriceCRUD()
        tickers = ["BTC_USD", "ETH_USD"]

        for ticker in tickers:
            try:
                price = await client.get_index_price(ticker)  # converts internally
                ts = int(time.time())
                crud.create(db, ticker, price, ts)
                print(f"[+] Saved {ticker} = {price} at {ts}")
            except Exception as e:
                print(f"[-] Error fetching {ticker}: {e}")
        db.close()

    asyncio.run(_fetch())
