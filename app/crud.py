from sqlalchemy.orm import Session
from . import models

def get_available_cars(db: Session, day):
    booked = db.query(models.Booking.car_id)\
               .filter(models.Booking.date == day)
    return db.query(models.Car)\
             .filter(models.Car.id.notin_(booked))\
             .all()

def get_or_create_customer(db: Session, name: str):
    customer = db.query(models.Customer)\
                 .filter_by(name=name)\
                 .first()
    if not customer:
        customer = models.Customer(name=name)
        db.add(customer)
        db.commit()
        db.refresh(customer)
    return customer

def create_booking(db: Session, booking):
    exists = db.query(models.Booking)\
               .filter_by(car_id=booking.car_id, date=booking.date)\
               .first()
    if exists:
        return None

    customer = get_or_create_customer(db, booking.customer_name)

    new_booking = models.Booking(
        car_id=booking.car_id,
        customer_id=customer.id,
        date=booking.date
    )
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking
