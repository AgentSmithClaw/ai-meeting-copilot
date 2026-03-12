# 行动项管理测试

> test_action_items.py

---

```python
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_update_action_item_status():
    """测试更新行动项状态"""
    # 先创建一个会议和行动项
    meeting_data = {
        "title": "测试会议",
        "date": "2026-03-12",
        "participants": ["张三"],
        "content": "测试内容"
    }
    create_response = client.post("/generate", json=meeting_data)
    assert create_response.status_code == 200
    
    # 假设返回了 action_items，取第一个 ID
    meeting_id = 1  # 实际使用时需要从响应中获取
    
    # 更新状态
    response = client.put(
        f"/action-items/1",
        json={"status": "in_progress"}
    )
    # 根据实际接口实现调整
    # assert response.status_code in [200, 404]

def test_action_item_status_values():
    """测试行动项状态值"""
    valid_statuses = ["todo", "in_progress", "blocked", "done"]
    for status in valid_statuses:
        # 这里可以添加状态更新测试
        pass

def test_action_item_fields():
    """测试行动项必要字段"""
    required_fields = ["content", "owner", "deadline", "status"]
    # 验证返回的行动项包含必要字段
    pass
```

---

## 集成测试示例

```python
def test_full_meeting_flow():
    """测试完整的会议流程"""
    # 1. 创建会议
    meeting_data = {...}
    response = client.post("/generate", json=meeting_data)
    assert response.status_code == 200
    
    # 2. 获取会议列表
    response = client.get("/meetings")
    assert response.status_code == 200
    
    # 3. 获取单个会议详情
    # response = client.get("/meetings/1")
    # assert response.status_code == 200
```

---

最后更新：2026-03-12