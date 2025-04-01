import sys
print(*sys.path, sep="\n")

from fastapi.testclient import TestClient

from fastapi_service.main import app


client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to my FastAPI Service!"}

def test_hello():
    response = client.get("/hello/ChatGPT")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, ChatGPT!"}
