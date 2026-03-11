# AI Meeting Copilot for Business Teams

An AI-powered meeting copilot that turns raw meeting notes into structured summaries, key decisions, action items, risks, and next steps.

## Overview
Teams often lose execution quality after meetings because notes are scattered, action items are unclear, and historical discussions are hard to retrieve. This project is designed to solve that problem by transforming unstructured meeting content into a clear, reusable workflow output.

## Core Features
- Generate structured meeting summaries from raw notes
- Extract key decisions automatically
- Identify action items, owners, and deadlines
- Capture risks and pending issues
- Save and review historical meeting records
- Export meeting output in Markdown-friendly format

## Use Cases
- Project weekly syncs
- Cross-functional coordination meetings
- Product requirement reviews
- Internal planning sessions
- Research and discussion meetings

## Current Scope
This repository currently contains the first public MVP scaffold, including:
- Backend API prototype
- Basic frontend input page
- Sample meeting notes
- Product requirement draft

## Tech Stack
- **Frontend:** HTML / future upgrade to Next.js
- **Backend:** FastAPI
- **Database:** SQLite
- **LLM Layer:** Planned support for OpenAI / OpenRouter

## Output Structure
Each generated meeting result is organized into:
- Summary
- Key Decisions
- Action Items
- Risks / Open Questions
- Next Steps

## Repository Structure
```bash
ai-meeting-copilot/
├── backend/
│   ├── main.py
│   └── requirements.txt
├── docs/
│   └── PRD.md
├── frontend/
│   └── index.html
├── samples/
│   └── sample-meeting-notes.md
└── README.md
```

## Getting Started
### 1. Start backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### 2. Open frontend
Open `frontend/index.html` in your browser.

## Roadmap
### Phase 1
- [x] Project scaffold
- [x] API prototype
- [x] Basic input page
- [x] Sample data

### Phase 2
- [ ] Improve structured output quality
- [ ] Add meeting history page
- [ ] Add action item management view
- [ ] Clean up frontend UX

### Phase 3
- [ ] Integrate real LLM calls
- [ ] Add audio-to-text workflow
- [ ] Add notifications / reminders
- [ ] Add polished portfolio demo assets

## Product Direction
This project is intended to become a practical business productivity tool rather than a toy demo. The goal is to build a portfolio-grade application that demonstrates:
- AI-assisted information structuring
- workflow efficiency improvement
- action-item tracking
- product thinking for collaboration scenarios

## Status
Early public portfolio version. Under active iteration.
