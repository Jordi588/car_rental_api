from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..schemas import BookingCreate
from ..crud import create_booking
from ..logging_conf import logger

router = APIRouter(prefix="/bookings", tags=["bookings"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("")
def book_car(booking: BookingCreate, db: Session = Depends(get_db)):
    result = create_booking(db, booking)
    if not result:
        logger.warning("Failed booking attempt")
        raise HTTPException(status_code=400, detail="Car already booked")
    logger.info("Successful booking")
    return result
