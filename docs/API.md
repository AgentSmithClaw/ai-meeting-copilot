# ai-meeting-copilot API Documentation

> FastAPI 后端接口文档

---

## Base URL
```
http://127.0.0.1:8000
```

---

## Endpoints

### 1. 健康检查

**GET** `/health`

检查服务是否正常运行。

**Response:**
```json
{
  "status": "ok"
}
```

---

### 2. 生成会议纪要

**POST** `/generate`

输入会议内容，生成结构化纪要。

**Request:**
```json
{
  "title": "项目周会",
  "date": "2026-03-12",
  "participants": ["张三", "李四", "王五"],
  "content": "会议内容文本..."
}
```

**Response:**
```json
{
  "summary": "本周主要讨论了项目进度...",
  "conclusions": [
    "确认下周完成UI设计",
    "后端接口需要提前对接"
  ],
  "action_items": [
    {
      "content": "完成登录页面",
      "owner": "张三",
      "deadline": "2026-03-15",
      "status": "todo"
    }
  ],
  "risks": [
    "前端资源可能不足"
  ],
  "next_steps": [
    "周三前确认设计稿",
    "周五进行接口评审"
  ]
}
```

---

### 3. 获取历史会议列表

**GET** `/meetings`

获取所有历史会议记录。

**Response:**
```json
{
  "meetings": [
    {
      "id": "1",
      "title": "项目周会",
      "date": "2026-03-12",
      "created_at": "2026-03-12T10:00:00"
    }
  ]
}
```

---

### 4. 获取单个会议详情

**GET** `/meetings/{meeting_id}`

根据ID获取会议详情。

**Response:**
```json
{
  "id": "1",
  "title": "项目周会",
  "date": "2026-03-12",
  "participants": ["张三", "李四"],
  "content": "原始会议内容",
  "result": {
    "summary": "...",
    "conclusions": [...],
    "action_items": [...],
    "risks": [...],
    "next_steps": [...]
  }
}
```

---

### 5. 更新行动项状态

**PUT** `/action-items/{item_id}`

更新行动项的状态。

**Request:**
```json
{
  "status": "in_progress"
}
```

**Status Options:**
- `todo`
- `in_progress`
- `blocked`
- `done`

---

### 6. 删除会议

**DELETE** `/meetings/{meeting_id}`

删除指定会议记录。

---

## 数据模型

### Meeting
```python
class Meeting:
    id: str
    title: str
    date: str
    participants: List[str]
    content: str
    result: MeetingResult
    created_at: datetime
```

### MeetingResult
```python
class MeetingResult:
    summary: str
    conclusions: List[str]
    action_items: List[ActionItem]
    risks: List[str]
    next_steps: List[str]
```

### ActionItem
```python
class ActionItem:
    id: str
    content: str
    owner: str
    deadline: str
    status: str  # todo, in_progress, blocked, done
```

---

## 错误处理

所有接口可能返回以下错误：

| 状态码 | 说明 |
|---|---|
| 400 | 请求参数错误 |
| 404 | 资源不存在 |
| 500 | 服务器内部错误 |

---

最后更新：2026-03-12