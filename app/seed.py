import json
from pathlib import Path
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Car, Customer, Booking

DATA_DIR = Path("app/data")

def load_json(name):
    with open(DATA_DIR / name) as f:
        return json.load(f)

def seed_database():
    db: Session = SessionLocal()

    if db.query(Car).first():
        db.close()
        return

    for car in load_json("cars.json"):
        db.add(Car(**car))
    db.commit()

    for cust in load_json("customers.json"):
        db.add(Customer(**cust))
    db.commit()

    for booking in load_json("bookings.json"):
        db.add(Booking(**booking))
    db.commit()

    db.close()
    print("Database seeded")
