from fastapi.testclient import TestClient
from recoverypilot_api.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_chat() -> None:
    response = client.post(
        "/chat",
        json={"message": "Help me recover access to a bank payment record."},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["case"]["asset_type"] == "financial_asset"
    assert data["reply"]
    assert data["next_actions"]
