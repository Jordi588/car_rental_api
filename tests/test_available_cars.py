from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_available_cars():
    response = client.get("/cars/available?date=2026-01-01")
    assert response.status_code == 200
