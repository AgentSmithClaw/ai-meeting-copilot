# ai-meeting-copilot Docker 支持

> 使用 Docker 快速部署项目

---

## Dockerfile

在 `backend/Dockerfile` 创建：

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件
COPY requirements.txt .

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# 暴露端口
EXPOSE 8000

# 启动命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## requirements.txt

```txt
fastapi>=0.100.0
uvicorn>=0.23.0
pydantic>=2.0.0
sqlalchemy>=2.0.0
python-multipart>=0.0.6
```

---

## docker-compose.yml

在项目根目录创建 `docker-compose.yml`：

```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    volumes:
      - ./backend:/app
    environment:
      - DATABASE_URL=sqlite:///./meetings.db

  frontend:
    image: nginx:alpine
    ports:
      - "8080:80"
    volumes:
      - ./frontend:/usr/share/nginx/html
```

---

## 使用方法

### 构建并启动
```bash
docker-compose up --build
```

### 后台运行
```bash
docker-compose up -d
```

### 查看日志
```bash
docker-compose logs -f
```

### 停止
```bash
docker-compose down
```

---

## 注意事项

- 确保 Docker 已安装
- 前端需要单独配置或使用静态文件服务器
- 数据库文件需要持久化

---

最后更新：2026-03-12