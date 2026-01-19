from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
from ..database import SessionLocal
from ..crud import get_available_cars

router = APIRouter(prefix="/cars", tags=["cars"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/available")
def available_cars(date: date, db: Session = Depends(get_db)):
    return get_available_cars(db, date)
