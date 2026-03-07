#!/bin/bash
set -e

echo "Starting Deribit Price Tracker"

# Start FastAPI
uvicorn app.main:app --host 0.0.0.0 --port 8000 &

# Start Celery worker
celery -A app.celery_app worker --loglevel=info &

# Start Celery beat (the scheduler)
celery -A app.celery_app beat --loglevel=info &

# Keep the container alive
wait
