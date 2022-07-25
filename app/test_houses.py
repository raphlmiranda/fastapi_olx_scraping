from .api import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_health():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_houses_list():
    response = client.get("/api/v1/olx/houses")
    assert response.status_code == 200
    assert len(response.json()) == 50

def test_houses_by_id():
    response = client.get("/api/v1/olx/houses/1")
    assert response.status_code == 200
