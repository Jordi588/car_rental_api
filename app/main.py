from fastapi import FastAPI
from .database import Base, engine
from .seed import seed_database
from .routers import cars, bookings
from .logging_conf import logger

app = FastAPI(title="Car Rental API")

@app.on_event("startup")
def startup():
    logger.info("Creating tables...")
    Base.metadata.create_all(bind=engine)

    logger.info("Running database seed...")
    seed_database()

app.include_router(cars.router)
app.include_router(bookings.router)

@app.get("/")
def health():
    logger.info("Healthcheck requested")
    return {"status": "ok"}

