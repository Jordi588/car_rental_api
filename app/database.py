from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import time

DATABASE_URL = os.getenv("DATABASE_URL")

# Retry loop for DB connection
for _ in range(5):
    try:
        engine = create_engine(DATABASE_URL, future=True)
        break
    except Exception:
        time.sleep(2)

SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()

