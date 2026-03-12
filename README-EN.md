# ai-meeting-copilot

<div align="center">

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![FastAPI](https://img.shields.io/badge/backend-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3.9+-3776AB.svg)](https://www.python.org/)
[![Stars](https://img.shields.io/github/stars/AgentSmithClaw/ai-meeting-copilot?style=social)](https://github.com/AgentSmithClaw/ai-meeting-copilot)

**AI Meeting Minutes & Action Item Assistant**

Transform raw meeting notes into structured summaries, key conclusions, action items, risks, and next steps.

</div>

---

## 📖 Overview

`ai-meeting-copilot` is an AI-powered tool focused on **team collaboration efficiency**.

Many teams face this problem after meetings:
- Meeting notes are scattered
- Key conclusions are not captured
- Action items are unclear
- Responsibilities and deadlines are undefined
- Historical meetings are hard to search
- Execution often falls through the cracks

This project's goal is to convert **unstructured meeting records** into **structured, executable, and trackable** outputs, helping teams improve communication efficiency and execution quality.

---

## ✨ Features

- 📝 **Structured Meeting Summary** - Auto-organize summary, conclusions, risks, and next steps
- ✅ **Action Item Extraction** - Extract tasks, owners, deadlines, and status
- 🔍 **Historical Search** - Save and search meeting history
- 📦 **Export Ready** - Output in Markdown/document-friendly format
- ⚡ **API Design** - Easy to integrate with frontend, notification systems, and LLMs
- 🧩 **Extensible** - Voice-to-text, notifications, platform integration ready

---

## 🛠️ Tech Stack

| Module | Technology |
|--------|------------|
| Frontend | HTML (Next.js planned) |
| Backend | FastAPI |
| Database | SQLite |
| LLM | Planned: OpenAI / OpenRouter |
| Format | JSON / Markdown |

---

## 🚀 Quick Start

```bash
# Clone the project
git clone https://github.com/AgentSmithClaw/ai-meeting-copilot.git
cd ai-meeting-copilot

# Install dependencies
cd backend
pip install -r requirements.txt

# Start backend
uvicorn main:app --reload

# Open frontend
# Open frontend/index.html in browser
```

---

## 📁 Project Structure

```
ai-meeting-copilot/
├── backend/
│   ├── main.py               # FastAPI backend
│   └── requirements.txt      # Python dependencies
├── docs/
│   ├── PRD.md               # Product requirements
│   ├── phase3-progress.md  # Phase 3 progress
│   └── demo-materials.md    # Demo materials
├── frontend/
│   └── index.html            # Frontend prototype
├── samples/
│   └── sample-meeting-notes.md  # Sample data
└── README.md
```

---

## 🗺️ Roadmap

### Phase 1 ✅
- [x] Project skeleton
- [x] FastAPI prototype
- [x] Basic frontend
- [x] Sample data

### Phase 2 🔄
- [ ] Improve output quality
- [ ] Add history page
- [ ] Add action item management
- [ ] Polish UI

### Phase 3 📋
- [ ] Integrate real LLM
- [ ] Add voice-to-text
- [ ] Add notification system
- [ ] Complete demo materials

---

## 📌 Status

**Current**: First version public portfolio project, continuously iterating.

**Next**: Upgrade from "public skeleton" to "demonstratable MVP", then to "formal portfolio version".

---

## 📧 Contact

- GitHub: https://github.com/AgentSmithClaw
- Email: [Your Email]

---

<div align="center">

Made for portfolio, product thinking, and AI workflow practice.

</div>