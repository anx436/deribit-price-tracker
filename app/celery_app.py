from celery import Celery
from app.core.config import settings
from celery.schedules import crontab

celery_app = Celery(
    "deribit_tasks",
    # broker=settings.REDIS_URL,
    # backend=settings.REDIS_URL,
    broker=settings.RABBITMQ_URL,
    backend="rpc://", 
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

celery_app.autodiscover_tasks(["app.tasks.prices"])

# Every minute
celery_app.conf.beat_schedule = {
    "fetch-prices-every-minute": {
        "task": "app.tasks.prices.fetch_and_save_prices",
        "schedule": 60.0,          # every 60 seconds
    },
}
