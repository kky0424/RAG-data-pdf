# Intelligent Q&A System for PDF Papers Based on RAG

## Technology Stack

- **Backend**: Flask + DeepSeek + SiliconFlow
- **Frontend**: Vue 3 + Element Plus + Vite
- **Vectorization**: BAAI/bge-large-zh-v1.5
- **PDF Processing**: PyPDF2

## Project Structure

```
.
├── src/
│   ├── backend/              # Backend Code
│   │   ├── config/          # Configuration Management
│   │   ├── services/        # Core Services
│   │   ├── routes/          # API Routes
│   │   └── app.py          # Flask Entry Point
│   ├── frontend/            # Frontend Code
│   │   └── src/
│   │       ├── components/  # Vue Components
│   │       └── api/        # API Calls
│   └── data/               # Data Storage
│       ├── uploads/        # Uploaded PDFs
│       └── vector_db/      # Vector Database
```

## Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+
- Conda environment (recommended)

### 1. Start Backend

```bash
# Activate conda flask environment
conda activate flask

# Install dependencies (if needed)
pip install flask flask-cors PyPDF2 requests numpy

# Start backend service
python -m src.backend.app
```

Backend will run at `http://localhost:5000`

### 2. Start Frontend

```bash
# Navigate to frontend directory
cd src/frontend

# Install dependencies (first time)
npm install

# Start development server
npm run dev
```

Frontend will run at `http://localhost:3000`

### 3. Access System

Open `http://localhost:3000` in your browser

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/upload` | POST | Upload PDF file |
| `/api/ask` | POST | Ask questions |
| `/api/stats` | GET | Get statistics |
| `/api/clear` | POST | Clear knowledge base |

### Configuration Parameters

Adjustable in `src/backend/config/settings.py`:

- `CHUNK_SIZE`: Text chunk size (default: 500)
- `CHUNK_OVERLAP`: Chunk overlap size (default: 50)
- `TOP_K`: Number of retrieved documents (default: 3)

# 基于RAG的PDF论文智能问答系统



## 技术栈

- **后端**: Flask + DeepSeek + SiliconFlow
- **前端**: Vue 3 + Element Plus + Vite
- **向量化**: BAAI/bge-large-zh-v1.5
- **PDF处理**: PyPDF2

## 项目结构

```
.
├── src/
│   ├── backend/              # 后端代码
│   │   ├── config/          # 配置管理
│   │   ├── services/        # 核心服务
│   │   ├── routes/          # API路由
│   │   └── app.py          # Flask入口
│   ├── frontend/            # 前端代码
│   │   └── src/
│   │       ├── components/  # Vue组件
│   │       └── api/        # API调用
│   └── data/               # 数据存储
│       ├── uploads/        # 上传的PDF
│       └── vector_db/      # 向量数据库

```

## 快速开始

### 前置要求

- Python 3.8+
- Node.js 16+
- conda环境（推荐）

### 1. 启动后端

```bash
# 激活conda的flask环境
conda activate flask

# 安装依赖（如需要）
pip install flask flask-cors PyPDF2 requests numpy

# 启动后端服务
python -m src.backend.app
```

后端将运行在 `http://localhost:5000`

### 2. 启动前端

```bash
# 进入前端目录
cd src/frontend

# 安装依赖（首次运行）
npm install

# 启动开发服务器
npm run dev
```

前端将运行在 `http://localhost:3000`

### 3. 访问系统

在浏览器中打开 `http://localhost:3000`


## API接口

| 端点 | 方法 | 说明 |
|------|------|------|
| `/api/upload` | POST | 上传PDF文件 |
| `/api/ask` | POST | 提问 |
| `/api/stats` | GET | 获取统计信息 |
| `/api/clear` | POST | 清空知识库 |


### 参数配置

在 `src/backend/config/settings.py` 中可调整：

- `CHUNK_SIZE`: 文本分块大小（默认500）
- `CHUNK_OVERLAP`: 分块重叠大小（默认50）
- `TOP_K`: 检索文档数量（默认3）


