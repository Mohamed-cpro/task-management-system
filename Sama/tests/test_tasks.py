from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_get_tasks_unauthorized():
    response = client.get("/tasks")
    assert response.status_code == 403 or response.status_code == 401