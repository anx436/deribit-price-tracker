# =============================================
# MINIMAL SQLALCHEMY CONNECTION TEST
# Run this BEFORE uvicorn to debug the DB error
# =============================================

import sys
from sqlalchemy import create_engine, text
from app.core.config import settings

print("DATABASE TEST STARTED")
print(f"   Using DATABASE_URL = {settings.DATABASE_URL}")
print("-" * 60)

try:
    engine = create_engine(settings.DATABASE_URL, echo=False)
    
    # Test actual connection
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1 as test"))
        print("DATABASE CONNECTION SUCCESSFUL!")
        print(f"Server responded with: {result.scalar()}")
        
        # Also test table creation (same as main.py)
        from app.core.database import Base
        from app.models.price import Price
        Base.metadata.create_all(bind=engine)
        print("Tables created (or already existed)")

    print("\nEverything works! You can now run uvicorn.")

except Exception as e:
    print("CONNECTION FAILED")
    print(f"   Error type: {type(e).__name__}")
    print(f"   Message: {e}")
    print("\nQUICK FIXES:")
    print("   1. Make sure PostgreSQL is running:   sudo systemctl status postgresql")
    print("   2. Your .env MUST contain this line:")
    print("      DATABASE_URL=postgresql+psycopg://user:pass@localhost:5432/deribit")

http://127.0.0.1:8000/prices/filter?ticker=BTC_USD&start=0
    print("   3. Did you run these commands earlier?")
    print("      sudo -u postgres createuser -d -P user     # password = pass")
    print("      sudo -u postgres createdb -O user deribit")
    print("   4. Restart PostgreSQL: sudo systemctl restart postgresql")
    
    sys.exit(1)
