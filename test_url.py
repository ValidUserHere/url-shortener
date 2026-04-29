from fastapi.testclient import TestClient
from url_sh import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_shorten_valid_url():
    response = client.post("/shorten", json={"url": "https://google.com"})
    assert response.status_code == 200
    assert "short_code" in response.json()

def test_shorten_invalid_url():
    response = client.post("/shorten", json={"url": "notaurl"})
    assert response.status_code == 422

def test_redirect_valid_code():
    shorten = client.post("/shorten", json={"url": "https://google.com"})
    code = shorten.json()["short_code"]
    response = client.get(f"/{code}", follow_redirects=False)
    assert response.status_code == 307

def test_redirect_invalid_code():
    response = client.get("/fakecode")
    assert response.status_code == 404