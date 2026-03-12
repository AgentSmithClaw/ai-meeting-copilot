# 🤖 ai-meeting-copilot

<div align="center">

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![FastAPI](https://img.shields.io/badge/backend-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![Portfolio Project](https://img.shields.io/badge/type-Portfolio%20Project-purple.svg)](#)

**一个面向企业团队的 AI 会议纪要与行动项助手**

把原始会议记录整理成结构化纪要、关键结论、行动项、风险事项和下一步安排。

</div>

---

## 📖 项目简介

`ai-meeting-copilot` 是一个聚焦 **会议协同效率** 的 AI 应用项目。

很多团队在开会之后，真正的问题不是“没讨论”，而是：

- 会议内容记录零散
- 关键结论没有沉淀
- 行动项不清晰
- 负责人和截止时间不明确
- 历史会议难以检索
- 会后执行容易断层

这个项目的目标，就是把 **非结构化会议记录** 转换成 **结构化、可执行、可跟踪** 的会议输出，帮助团队提升沟通效率和执行闭环质量。

---

## ✨ 功能特性

- 📝 **结构化会议纪要生成** - 自动整理摘要、结论、风险与下一步安排
- ✅ **行动项提取** - 自动提取任务、负责人、截止时间、状态
- 🔍 **历史会议可追溯** - 支持保存和查看历史会议记录
- 📦 **结果可导出** - 输出适合 Markdown / 文档整理的格式
- ⚡ **API 化设计** - 便于后续接入前端、提醒系统和真实大模型
- 🧩 **适合扩展** - 后续可接语音转文字、通知提醒、协同平台集成

---

## 🎯 适用场景

- 项目周会
- 跨部门协同会
- 产品需求评审会
- 内部规划讨论会
- 研究讨论类会议
- 日常执行跟进会

---

## 📁 目录结构

```bash
ai-meeting-copilot/
├── backend/
│   ├── main.py               # FastAPI 后端原型
│   └── requirements.txt      # Python 依赖
├── docs/
│   └── PRD.md                # 产品需求文档
├── frontend/
│   └── index.html            # 当前前端页面原型
├── samples/
│   └── sample-meeting-notes.md  # 样例会议记录
└── README.md
```

---

## 🛠️ 技术栈

| 模块 | 技术 |
|------|------|
| 前端 | HTML（后续计划升级为 Next.js） |
| 后端 | FastAPI |
| 数据库 | SQLite |
| 模型接入 | 计划支持 OpenAI / OpenRouter |
| 数据格式 | JSON / Markdown |

---

## 🧱 当前已实现内容

### 第一阶段（已完成）
- [x] 项目骨架初始化
- [x] FastAPI 后端原型
- [x] 基础前端输入页
- [x] 样例会议记录准备
- [x] PRD 初稿
- [x] GitHub 公开仓库上线

### 当前 MVP 能力
- 输入会议标题、日期、参会人、会议记录
- 返回结构化会议结果
- 保存会议记录到本地 SQLite
- 查看历史会议记录接口

---

## 📤 输出结构

每次生成的会议结果默认包含以下模块：

- **会议摘要**
- **关键结论**
- **行动项**
- **风险 / 待确认事项**
- **下一步安排**

这套结构的设计目标是：
**减少信息损耗，让会议结果可以直接进入执行阶段。**

---

## 🚀 快速开始

### 1）启动后端

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### 2）打开前端页面

直接在浏览器中打开：

```bash
frontend/index.html
```

### 3）输入样例会议记录进行测试

可以先使用：

```bash
samples/sample-meeting-notes.md
```

中的样例内容进行演示。

---

## 🗺️ 路线图

### 第二阶段（进行中）
- [ ] 提升结构化输出质量
- [ ] 增加历史会议页面
- [ ] 增加行动项管理视图
- [ ] 优化前端展示效果
- [ ] 提升作品集级别的界面完成度

### 第三阶段（进行中）
- [ ] 接入真实大模型调用
- [ ] 增加音频转文字流程
- [x] 增加提醒 / 通知能力（设计已完成）
- [x] 输出更完整的演示素材（Demo脚本完善中）
- [x] 整理成正式作品集项目（进行中）

---

## 💡 产品方向

这个项目不是一个单纯的玩具 demo，而是一个偏 **业务协同效率工具** 的作品集项目。

核心想表达的能力包括：

- AI 在协作场景中的产品化落地能力
- 信息整理与结构化能力
- 行动项闭环设计能力
- 从会议讨论到执行追踪的流程思维

---

## 📌 当前状态

当前为 **第一版公开作品集项目**，正在持续迭代中。  
下一步重点是把它从“公开骨架”升级成“可展示 MVP”，再进一步升级为“正式作品集版本”。

---

<div align="center">

Made for portfolio, product thinking, and AI workflow practice.

</div>
