import sys
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"ok": True}


def test_generate_meeting():
    response = client.post(
        "/meetings/generate",
        json={
            "title": "Weekly sync",
            "meeting_date": "2026-03-12",
            "participants": ["Alice", "Bob"],
            "raw_notes": "Alice will submit the launch checklist by Friday.",
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert data["summary"]
    assert isinstance(data["action_items"], list)
    assert isinstance(data["key_decisions"], list)
