import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/api/portfolio/health")
    assert response.status_code == 200
    assert response.json()["status"] == "Risk engine healthy"

def test_hsbc_risk():
    response = client.get("/api/risk/hsbc")
    assert response.status_code == 200
    data = response.json()
    assert "pnl" in data
    assert data["symbol"] == "0005.HK (HSBC)"
    assert isinstance(data["var_95"], (int, float))

def test_portfolio_analyze():
    portfolio_data = {
        "positions": [{
            "symbol": "0005.HK",
            "quantity": 1000,
            "avg_price": 65.0,
            "current_price": 67.0,
            "asset_class": "EQUITY"
        }],
        "cash": 100000
    }
    response = client.post("/api/portfolio/analyze", json=portfolio_data)
    assert response.status_code == 200
    assert "total_pnl" in response.json()
