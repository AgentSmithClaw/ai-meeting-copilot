import sys
from pathlib import Path

from fastapi.testclient import TestClient
from sqlmodel import SQLModel

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from main import app, engine


SQLModel.metadata.create_all(engine)
client = TestClient(app)


def test_create_meeting_and_update_action_item():
    create_response = client.post(
        "/meetings",
        json={
            "title": "Planning",
            "meeting_date": "2026-03-12",
            "participants": ["Alice"],
            "raw_notes": "Alice will prepare the roadmap by next week.",
        },
    )
    assert create_response.status_code == 200

    meeting_id = create_response.json()["id"]
    update_response = client.patch(
        f"/meetings/{meeting_id}/action-items/0",
        json={"status": "in_progress"},
    )

    assert update_response.status_code == 200
    meeting = update_response.json()["meeting"]
    assert meeting["action_items"][0]["status"] == "in_progress"


def test_update_missing_action_item_returns_404():
    response = client.patch(
        "/meetings/999999/action-items/0",
        json={"status": "in_progress"},
    )

    assert response.status_code == 404
