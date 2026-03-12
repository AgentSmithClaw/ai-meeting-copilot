# 单元测试示例

> ai-meeting-copilot 后端测试用例

---

## 安装测试依赖

```bash
pip install pytest pytest-asyncio httpx
```

---

## 测试文件结构

```
backend/
├── tests/
│   ├── __init__.py
│   ├── test_meetings.py
│   └── test_action_items.py
└── main.py
```

---

## 测试示例

### test_meetings.py

```python
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    """测试健康检查接口"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_generate_meeting():
    """测试会议生成接口"""
    meeting_data = {
        "title": "测试会议",
        "date": "2026-03-12",
        "participants": ["张三", "李四"],
        "content": "测试会议内容"
    }
    response = client.post("/generate", json=meeting_data)
    assert response.status_code == 200
    data = response.json()
    assert "summary" in data
    assert "action_items" in data

def test_get_meetings():
    """测试获取会议列表"""
    response = client.get("/meetings")
    assert response.status_code == 200
    data = response.json()
    assert "meetings" in data

def test_get_meeting_not_found():
    """测试获取不存在的会议"""
    response = client.get("/meetings/99999")
    assert response.status_code == 404
```

---

## 运行测试

```bash
# 运行所有测试
pytest

# 运行指定文件
pytest tests/test_meetings.py

# 显示详细输出
pytest -v

# 显示覆盖率
pytest --cov=. --cov-report=html
```

---

## 测试原则

1. **Arrange**: 准备测试数据
2. **Act**: 执行被测函数
3. **Assert**: 验证结果

4. 每个测试函数只测试一个功能
5. 测试名称要清晰描述测试内容
6. 保持测试独立性

---

最后更新：2026-03-12