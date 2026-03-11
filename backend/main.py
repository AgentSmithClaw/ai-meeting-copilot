from datetime import datetime
from typing import Optional, List

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Session, create_engine, select


app = FastAPI(title="AI Meeting Copilot API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = create_engine("sqlite:///meeting_copilot.db")


class Meeting(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    meeting_date: str
    participants: str
    raw_notes: str
    summary: str = ""
    key_decisions: str = ""
    action_items: str = ""
    risks: str = ""
    next_steps: str = ""
    created_at: datetime = Field(default_factory=datetime.utcnow)


class MeetingCreate(BaseModel):
    title: str
    meeting_date: str
    participants: List[str]
    raw_notes: str


class MeetingGenerateResponse(BaseModel):
    summary: str
    key_decisions: List[str]
    action_items: List[dict]
    risks: List[str]
    next_steps: List[str]


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


def mock_generate_structured_notes(payload: MeetingCreate) -> MeetingGenerateResponse:
    lines = [line.strip() for line in payload.raw_notes.splitlines() if line.strip()]
    summary = lines[0] if lines else "本次会议围绕项目推进与待办协同展开。"
    decisions = [
        "确认当前会议目标与优先事项",
        "需要形成行动项并明确负责人",
    ]
    action_items = [
        {
            "task": "整理会议纪要并同步团队",
            "owner": payload.participants[0] if payload.participants else "待定",
            "deadline": payload.meeting_date,
            "status": "未完成",
        }
    ]
    risks = ["部分事项负责人和截止时间仍需二次确认"]
    next_steps = ["会后确认行动项并在下次会议回顾执行情况"]
    return MeetingGenerateResponse(
        summary=summary,
        key_decisions=decisions,
        action_items=action_items,
        risks=risks,
        next_steps=next_steps,
    )


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/meetings/generate", response_model=MeetingGenerateResponse)
def generate_meeting(payload: MeetingCreate):
    return mock_generate_structured_notes(payload)


@app.post("/meetings")
def create_meeting(payload: MeetingCreate):
    generated = mock_generate_structured_notes(payload)
    meeting = Meeting(
        title=payload.title,
        meeting_date=payload.meeting_date,
        participants=", ".join(payload.participants),
        raw_notes=payload.raw_notes,
        summary=generated.summary,
        key_decisions="\n".join(generated.key_decisions),
        action_items="\n".join([str(item) for item in generated.action_items]),
        risks="\n".join(generated.risks),
        next_steps="\n".join(generated.next_steps),
    )
    with Session(engine) as session:
        session.add(meeting)
        session.commit()
        session.refresh(meeting)
    return {"id": meeting.id, "generated": generated}


@app.get("/meetings")
def list_meetings():
    with Session(engine) as session:
        meetings = session.exec(select(Meeting).order_by(Meeting.id.desc())).all()
    return meetings


@app.get("/meetings/{meeting_id}")
def get_meeting(meeting_id: int):
    with Session(engine) as session:
        meeting = session.get(Meeting, meeting_id)
        if not meeting:
            raise HTTPException(status_code=404, detail="Meeting not found")
    return meeting
