from fastapi.testclient import TestClient
from retrain.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'drift': True, 'age_days': 4}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'drift': False, 'age_days': 2}).json()
    assert bad["passed"] is False
    assert "no_retrain_needed" in bad["failed"]
