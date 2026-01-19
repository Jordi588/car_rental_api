from pydantic import BaseModel
from datetime import date

class BookingCreate(BaseModel):
    car_id: int
    date: date
    customer_name: str

class CarOut(BaseModel):
    id: int
    brand: str
    model: str

    class Config:
        orm_mode = True

