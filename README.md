# Deribit Price Tracker

Application that fetches **BTC_USD** and **ETH_USD** index prices from Deribit every minute and exposes them via a FastAPI.

** Characteristics :**
- Real-time price fetching with Celery
- Full FastAPI external API (3 GET endpoints)
- PostgreSQL database
- Docker deployment in 2 containers
- Unit + integration tests

---

## Quick Start

### Option 1: Docker

```bash
# 1. Make sure RabbitMQ is running on your machine
sudo systemctl start rabbitmq

# 2. Start the 2 containers
docker compose up --build
```

### Option 2: Native

```bash
uvicorn app.main:app --reload & #starts fastapi
celery -A app.celery_app worker --loglevel=info &
celery -A app.celery_app beat --loglevel=info &
```

## API Endpoints (all GET)All endpoints require the mandatory query parameter “ticker” (e.g. BTC_USD or ETH_USD).

Method     Endpoint                                      Description
GET        /prices/all?ticker=BTC_USD                    Get all saved prices
GET        /prices/latest?ticker=BTC_USD                 Get the latest price
GET        /prices/filter?ticker=BTC_USD&start=...       Get prices with UNIX timestamp filter

## Tech Stack

-   FastAPI – Modern async API
-   Celery – Periodic price fetching
-   RabbitMQ – Message broker
-   PostgreSQL – Database
-   SQLAlchemy – ORM
-   aiohttp – Deribit client
-   Pydantic – Settings & validation
-   Docker – 2-container deployment
-   pytest – Testing

