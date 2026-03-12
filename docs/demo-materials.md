# 项目演示素材

> ai-meeting-copilot 面试展示用素材包

---

## 1. 项目GitHub链接
- **仓库地址**：https://github.com/AgentSmithClaw/ai-meeting-copilot
- **个人作品集**：https://github.com/AgentSmithClaw/ai-job-search-playbook

---

## 2. 核心功能截图列表

| 序号 | 功能 | 截图文件 | 说明 |
|---|---|---|---|
| 1 | 会议输入页 | `01-input.png` | 用户输入会议信息的界面 |
| 2 | 结构化结果 | `02-result.png` | AI生成的纪要结果 |
| 3 | 历史会议列表 | `03-history.png` | 历史会议检索 |
| 4 | 行动项管理 | `04-action-items.png` | 状态管理与跟进 |
| 5 | 仪表盘统计 | `05-dashboard.png` | 数据统计视图 |

> 注：实际演示时可使用 `frontend/index.html` 进行现场演示

---

## 3. 1分钟项目讲解稿

"我做了一个AI会议纪要与行动项助手，叫 ai-meeting-copilot。
解决的问题是：团队开会后，行动项经常不清晰，责任人不明确，时间一长就忘了。
我的方案是：把非结构化的会议记录，自动转换成结构化纪要，包含结论、行动项、风险和下一步。
核心技术栈是 FastAPI + SQLite，前端用轻量HTML原型。
目前已经完成了MVP，可以演示。这是我的GitHub作品集地址。"

---

## 4. 常见面试问题回答

**Q: 这个项目技术栈偏简单？**
A: 这个项目的重点不是技术深度，而是产品思维。我更关注的是：
1. 识别真实业务痛点
2. 设计合适的信息结构
3. 思考如何让AI输出真正可执行
4. 理解从"功能"到"产品"的gap

**Q: 为什么不直接用市面上的产品？**
A: 市面上的会议产品更多关注"记录"，但很少解决"执行"问题。我这个项目的核心差异点是：把会议输出变成可追踪的行动项，而不是仅仅做信息沉淀。

**Q: 后续发展规划？**
A: 接下来我会：
1. 接入真实大模型提升输出质量
2. 增加提醒机制
3. 打磨成可直接展示的作品集版本

---

## 5. 快速启动命令

```bash
# 克隆项目
git clone https://github.com/AgentSmithClaw/ai-meeting-copilot.git
cd ai-meeting-copilot/backend

# 安装依赖
pip install -r requirements.txt

# 启动后端
uvicorn main:app --reload

# 打开前端
# 浏览器直接打开 frontend/index.html
```

---

## 6. 演示检查清单

- [ ] GitHub仓库可访问
- [ ] README清晰可读
- [ ] 本地可运行演示
- [ ] 1分钟讲稿可脱稿
- [ ] 常见问题已准备
- [ ] 项目代码结构整洁