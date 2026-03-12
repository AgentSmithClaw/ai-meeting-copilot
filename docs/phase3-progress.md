# ai-meeting-copilot 第三阶段：提醒机制与数据打磨

> 本阶段目标：完善提醒机制、打磨Demo、补充README安装说明

---

## 3.1 提醒机制设计

### 功能定义
当行动项即将到期或已超期时，通过系统提醒相关责任人。

### 数据模型
```python
class ReminderConfig:
    enabled: bool          # 是否启用提醒
    before_hours: int     # 提前提醒小时数（默认24h）
    channels: list         # 提醒渠道：["email", "web", "console"]
    
class ActionItem:
    # ... existing fields ...
    deadline: datetime     # 截止时间
    reminder_sent: bool    # 是否已发送提醒
    reminder_at: datetime  # 提醒发送时间
```

### 提醒触发逻辑
```
1. 定时任务每小时检查一次
2. 对于每个"进行中"的行动项：
   - 如果 (截止时间 - 当前时间) <= 提前小时数 且 未发送提醒
   - 则发送提醒并标记 reminder_sent = True
3. 如果 已超期 且 未发送提醒
   - 则发送超期提醒
```

### 提醒内容模板
```
【会议行动项提醒】
会议：{meeting_title}
行动项：{action_item_content}
截止时间：{deadline}
状态：{status}
剩余时间：{remaining_hours}小时
```

---

## 3.2 Demo演示脚本（完善版）

### 演示前检查清单
- [ ] 后端服务已启动（uvicorn main:app --reload）
- [ ] 前端页面可访问
- [ ] SQLite数据库已初始化
- [ ] 示例会议数据已导入
- [ ] 网络正常（如需调用API）

### 演示流程（3分钟版）

#### 0:00-0:20 开场（20秒）
"大家好，今天给大家演示的是 ai-meeting-copilot，一个面向团队协同场景的AI会议纪要与行动项助手。"

#### 0:20-0:50 问题引入（30秒）
"大家先思考一个问题：每次开完会后，是不是经常遇到这种情况——
会议记录有了，但行动项不清晰，责任人不明确，时间一长就忘了？
这个工具要解决的就是这个问题。"

#### 0:50-1:20 核心演示（30秒）
"现在我模拟输入一段会议内容。大家可以看到，我粘贴了一段会议纪要，现在点击‘生成结构化纪要’。"

"AI会自动提取出：结论、行动项、风险和下一步。每一项都结构化好了。"

#### 1:20-1:50 行动项管理（30秒）
"我们点开其中一个行动项——可以看到状态管理：待办/进行中/阻塞/完成。
我把它标记为‘进行中’。这样就能追踪每个行动项的进度。"

#### 1:50-2:20 历史与仪表盘（30秒）
"历史会议可以按时间检索。仪表盘能看到汇总数据：本周有多少会议、多少行动项、完成率怎么样。"

#### 2:20-2:50 提醒机制（30秒）
"第三阶段我们新增了提醒机制——当行动项即将到期时，系统会自动提醒责任人。
这个功能确保不会因为忘记而导致任务延误。"

#### 2:50-3:00 收尾（10秒）
"这就是整个产品的核心流程。目标就是让会议不只是‘记录’，而是真正变成可执行的‘行动’。谢谢大家！"

### 备用方案（如果Demo卡住）
- 准备静态截图作为fallback
- 提前录屏备用
- 准备本地运行版本供离线演示

---

## 3.3 README安装说明（完善版）

### 环境要求
- Python 3.9+
- 现代浏览器（Chrome/Edge/Safari）

### 安装步骤

#### 1. 克隆项目
```bash
git clone https://github.com/your-username/ai-meeting-copilot.git
cd ai-meeting-copilot
```

#### 2. 创建虚拟环境（推荐）
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

#### 3. 安装依赖
```bash
cd backend
pip install -r requirements.txt
```

#### 4. 启动后端
```bash
cd backend
uvicorn main:app --reload
```
后端运行在：http://127.0.0.1:8000

#### 5. 打开前端
直接在浏览器中打开：
```bash
frontend/index.html
```
或使用简易HTTP服务器：
```bash
cd frontend
python -m http.server 8080
```
然后访问：http://localhost:8080

#### 6. 验证安装
访问以下接口确认服务正常：
- http://127.0.0.1:8000/docs （FastAPI文档）
- http://127.0.0.1:8000/health （健康检查）

---

### 常见问题

**Q: 启动报错 "ModuleNotFoundError"?**
A: 确保已激活虚拟环境并执行 `pip install -r requirements.txt`

**Q: 前端无法连接到后端?**
A: 检查后端是否运行在8000端口，浏览器是否有跨域限制

**Q: 数据库初始化失败?**
A: 确保 backend 目录有写入权限

---

### API文档
启动后访问：http://127.0.0.1:8000/docs
可直接在页面上测试各API接口。

---

## 3.4 本阶段完成清单

- [x] 提醒机制设计方案
- [x] Demo脚本完善（3分钟版）
- [x] README安装说明
- [ ] 提醒功能代码实现
- [ ] 提醒定时任务接入
- [ ] 完整演示录屏素材