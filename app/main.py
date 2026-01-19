from fastapi import FastAPI
from .database import Base, engine
from .routers import cars, bookings

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Car Rental API")

app.include_router(cars.router)
app.include_router(bookings.router)

