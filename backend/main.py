from datetime import datetime
from typing import Optional, List
import json
import re

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


class ActionItem(BaseModel):
    task: str
    owner: str
    deadline: str
    status: str


class ActionItemUpdate(BaseModel):
    status: str


class MeetingGenerateResponse(BaseModel):
    summary: str
    key_decisions: List[str]
    action_items: List[ActionItem]
    risks: List[str]
    next_steps: List[str]


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


def _normalized_lines(raw_notes: str) -> List[str]:
    return [line.strip("-• ").strip() for line in raw_notes.splitlines() if line.strip()]


def _guess_owner(line: str, participants: List[str]) -> str:
    for participant in participants:
        if participant and participant in line:
            return participant
    owner_match = re.search(r"(?:负责人|owner|由)([:：]?)([^，。；,;]+)", line, re.IGNORECASE)
    if owner_match:
        return owner_match.group(2).strip()
    return participants[0] if participants else "待定"


def _guess_deadline(line: str, meeting_date: str) -> str:
    deadline_match = re.search(r"(\d{4}-\d{2}-\d{2}|\d{1,2}月\d{1,2}日|今天|明天|本周|下周)", line)
    if deadline_match:
        return deadline_match.group(1)
    return meeting_date


def _clean_task(line: str) -> str:
    line = re.sub(r"^(行动项|待办|TODO|Task)[:：]?", "", line, flags=re.IGNORECASE).strip()
    return line or "待补充行动项"


def _parse_json_field(value: str, fallback):
    try:
        return json.loads(value or "")
    except (json.JSONDecodeError, TypeError):
        return fallback


def mock_generate_structured_notes(payload: MeetingCreate) -> MeetingGenerateResponse:
    lines = _normalized_lines(payload.raw_notes)
    summary = "；".join(lines[:2]) if lines else "本次会议围绕项目推进、问题对齐与后续执行展开。"

    decisions = []
    action_items: List[ActionItem] = []
    risks = []
    next_steps = []

    action_keywords = ("行动项", "待办", "todo", "跟进", "完成", "推进", "提交", "整理", "输出", "安排", "确认")
    risk_keywords = ("风险", "阻塞", "问题", "卡点", "待确认", "依赖")
    decision_keywords = ("决定", "确认", "结论", "统一", "采用", "优先")
    next_step_keywords = ("下一步", "后续", "下周", "明天", "本周")

    for line in lines:
        lowered = line.lower()
        if any(keyword.lower() in lowered for keyword in action_keywords):
            action_items.append(
                ActionItem(
                    task=_clean_task(line),
                    owner=_guess_owner(line, payload.participants),
                    deadline=_guess_deadline(line, payload.meeting_date),
                    status="未完成",
                )
            )
        if any(keyword.lower() in lowered for keyword in risk_keywords):
            risks.append(line)
        if any(keyword.lower() in lowered for keyword in decision_keywords):
            decisions.append(line)
        if any(keyword.lower() in lowered for keyword in next_step_keywords):
            next_steps.append(line)

    if not decisions:
        decisions = [
            "确认当前阶段优先推进核心任务闭环",
            "统一将会议输出沉淀为可执行的行动项",
        ]

    if not action_items:
        action_items = [
            ActionItem(
                task="整理会议纪要并同步团队",
                owner=payload.participants[0] if payload.participants else "待定",
                deadline=payload.meeting_date,
                status="未完成",
            )
        ]

    if not risks:
        risks = ["部分事项的负责人、输入依赖或截止时间仍需进一步确认"]

    if not next_steps:
        next_steps = ["会后确认行动项优先级，并在下一次会议中回顾执行进度"]

    return MeetingGenerateResponse(
        summary=summary,
        key_decisions=decisions[:5],
        action_items=action_items[:10],
        risks=risks[:5],
        next_steps=next_steps[:5],
    )


def _meeting_to_detail(meeting: Meeting):
    return {
        "id": meeting.id,
        "title": meeting.title,
        "meeting_date": meeting.meeting_date,
        "participants": meeting.participants,
        "raw_notes": meeting.raw_notes,
        "summary": meeting.summary,
        "key_decisions": _parse_json_field(meeting.key_decisions, []),
        "action_items": _parse_json_field(meeting.action_items, []),
        "risks": _parse_json_field(meeting.risks, []),
        "next_steps": _parse_json_field(meeting.next_steps, []),
        "created_at": meeting.created_at,
    }


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
        key_decisions=json.dumps(generated.key_decisions, ensure_ascii=False),
        action_items=json.dumps([item.model_dump() for item in generated.action_items], ensure_ascii=False),
        risks=json.dumps(generated.risks, ensure_ascii=False),
        next_steps=json.dumps(generated.next_steps, ensure_ascii=False),
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
    return _meeting_to_detail(meeting)


@app.patch("/meetings/{meeting_id}/action-items/{action_index}")
def update_action_item_status(meeting_id: int, action_index: int, payload: ActionItemUpdate):
    with Session(engine) as session:
        meeting = session.get(Meeting, meeting_id)
        if not meeting:
            raise HTTPException(status_code=404, detail="Meeting not found")

        actions = _parse_json_field(meeting.action_items, [])
        if action_index < 0 or action_index >= len(actions):
            raise HTTPException(status_code=404, detail="Action item not found")

        actions[action_index]["status"] = payload.status
        meeting.action_items = json.dumps(actions, ensure_ascii=False)
        session.add(meeting)
        session.commit()
        session.refresh(meeting)

    return {"ok": True, "meeting": _meeting_to_detail(meeting)}


@app.get("/dashboard")
def dashboard():
    with Session(engine) as session:
        meetings = session.exec(select(Meeting).order_by(Meeting.id.desc())).all()

    parsed_meetings = []
    pending_actions = []
    for meeting in meetings:
        actions = _parse_json_field(meeting.action_items, [])
        decisions = _parse_json_field(meeting.key_decisions, [])

        parsed_meetings.append(
            {
                "id": meeting.id,
                "title": meeting.title,
                "meeting_date": meeting.meeting_date,
                "participants": meeting.participants,
                "summary": meeting.summary,
                "decision_count": len(decisions),
                "action_count": len(actions),
                "created_at": meeting.created_at,
            }
        )

        for index, action in enumerate(actions):
            if action.get("status") != "已完成":
                pending_actions.append(
                    {
                        "meeting_id": meeting.id,
                        "meeting_title": meeting.title,
                        "action_index": index,
                        **action,
                    }
                )

    return {
        "meeting_count": len(parsed_meetings),
        "pending_action_count": len(pending_actions),
        "recent_meetings": parsed_meetings[:10],
        "pending_actions": pending_actions[:20],
    }
