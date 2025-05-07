from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Witaj w API modelu ML!"}

def test_info():
    response = client.get("/info")
    assert response.status_code == 200
    data = response.json()
    assert data["model_type"] == "LogisticRegression"
    assert data["input_features"] == 2
    assert "sepal_length" in data["feature_names"]

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "OK"

def test_predict_valid_input():
    payload = {
        "sepal_length": 5.0,
        "sepal_width": 3.5
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert data["prediction"] in [0, 1]
    assert "probability" in data
    assert len(data["probability"]) == 2

def test_predict_invalid_input():
    payload = {
        "sepal_length": "not_a_number",
        "sepal_width": 3.5
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422 
