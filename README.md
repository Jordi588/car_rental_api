# car_rental_api

Car Rental REST API built with FastAPI.

Provides:
- List available cars by date
- Create car bookings

Stack:
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pytest

Run API:
- docker-compose -f docker-compose.yml up --build

Run Tests:
- docker-compose run --rm api pytest

Swagger UI:
- http://localhost:8000/docs
