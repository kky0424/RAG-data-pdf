# System Architecture Documentation

## Overview
RAG-based PDF Paper Intelligent Q&A System - A full-stack application for academic paper analysis and question answering

## Technology Stack

### Backend
- **Framework**: Flask (Python)
- **Large Language Model**: DeepSeek (answer generation)
- **Vectorization**: SiliconFlow BAAI/bge-large-zh-v1.5
- **Vector Storage**: Custom implementation based on numpy
- **PDF Processing**: PyPDF2

### Frontend
- **Framework**: Vue 3 + Vite
- **UI Component Library**: Element Plus

## Architecture Layers

### 1. Data Processing Layer
```
PDF Upload → Text Extraction → Cleaning → Chunking → Vectorization → Vector Storage
                                           ↓
                                     Metadata Extraction (NER)
```

### 2. Storage Layer
- **Vector Database**: `src/data/vector_db/vector_store.pkl`
- **Uploaded Files**: `src/data/uploads/`
- **Persistence**: Pickle serialization

### 3. Retrieval Layer
```
User Question → Question Vectorization → Cosine Similarity Search → Top-K Results
```

### 4. Generation Layer
```
Retrieved Context + Question → DeepSeek LLM → Answer + Sources
```

## Directory Structure

```
src/
├── backend/
│   ├── config/          # Configuration Management (API Keys, Paths)
│   ├── services/        # Core Business Logic
│   │   ├── pdf_processor.py      # PDF Text Extraction
│   │   ├── metadata_extractor.py # LLM-based Metadata Extraction
│   │   ├── embedder.py           # Text Vectorization
│   │   ├── vector_store.py       # Vector Database
│   │   └── rag_engine.py         # RAG Orchestration Engine
│   ├── routes/          # API Routes
│   └── app.py          # Flask Application Entry
├── frontend/
│   └── src/
│       ├── components/  # Vue Components
│       ├── api/        # API Client
│       └── main.js     # Entry File
└── data/               # Runtime Data
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/upload` | Upload and Process PDF |
| POST | `/api/ask` | Ask Questions |
| GET | `/api/stats` | Get Knowledge Base Statistics |
| POST | `/api/clear` | Clear Knowledge Base |

## Data Flow

### Upload Process
1. Frontend uploads PDF file
2. Backend extracts and cleans text
3. Text chunking (500 characters, 50 characters overlap)
4. LLM extracts metadata (title, authors, keywords)
5. Vectorize text chunks via SiliconFlow API
6. Store vectors in vector database

### Q&A Process
1. User submits question
2. Question vectorization
3. Vector database search for Top-K similar text chunks
4. Build context from retrieval results
5. DeepSeek generates contextual answer
6. Return answer and sources to frontend

## Key Design Decisions

- **Singleton Vector Store**: Upload and RAG engine share the same instance, ensuring data consistency
- **Batch Size = 1**: Prevent 413 errors from vectorization API
- **Max Text Length = 512**: Truncate long texts for API compatibility
- **Fixed Height Dialog**: 500px height with internal scrolling for better user experience
- **English Priority**: All prompts and responses use English for consistency

## Configuration Parameters

- **Chunk Size**: 500 characters
- **Chunk Overlap**: 50 characters
- **Retrieval Top-K**: 3 documents
- **Vectorization Model**: BAAI/bge-large-zh-v1.5
- **Large Language Model**: deepseek-chat
- **Temperature Parameter**: 0.7 (Q&A), 0.3 (metadata extraction)

# 系统架构文档

## 概述
基于RAG的PDF论文智能问答系统 - 用于学术论文分析和问答的全栈应用

## 技术栈

### 后端
- **框架**: Flask (Python)
- **大模型**: DeepSeek (答案生成)
- **向量化**: SiliconFlow BAAI/bge-large-zh-v1.5
- **向量存储**: 基于numpy的自定义实现
- **PDF处理**: PyPDF2

### 前端
- **框架**: Vue 3 + Vite
- **UI组件库**: Element Plus

## 架构层次

### 1. 数据处理层
```
PDF上传 → 文本提取 → 清洗 → 分块 → 向量化 → 向量存储
                           ↓
                    元数据提取 (NER)
```

### 2. 存储层
- **向量数据库**: `src/data/vector_db/vector_store.pkl`
- **上传文件**: `src/data/uploads/`
- **持久化**: Pickle序列化

### 3. 检索层
```
用户问题 → 问题向量化 → 余弦相似度搜索 → Top-K结果
```

### 4. 生成层
```
检索上下文 + 问题 → DeepSeek大模型 → 答案 + 来源
```

## 目录结构

```
src/
├── backend/
│   ├── config/          # 配置管理 (API密钥、路径)
│   ├── services/        # 核心业务逻辑
│   │   ├── pdf_processor.py      # PDF文本提取
│   │   ├── metadata_extractor.py # 基于LLM的元数据提取
│   │   ├── embedder.py           # 文本向量化
│   │   ├── vector_store.py       # 向量数据库
│   │   └── rag_engine.py         # RAG编排引擎
│   ├── routes/          # API路由
│   └── app.py          # Flask应用入口
├── frontend/
│   └── src/
│       ├── components/  # Vue组件
│       ├── api/        # API客户端
│       └── main.js     # 入口文件
└── data/               # 运行时数据
```

## API接口

| 方法 | 端点 | 描述 |
|------|------|------|
| POST | `/api/upload` | 上传并处理PDF |
| POST | `/api/ask` | 提问 |
| GET | `/api/stats` | 获取知识库统计 |
| POST | `/api/clear` | 清空知识库 |

## 数据流

### 上传流程
1. 前端上传PDF文件
2. 后端提取文本并清洗
3. 文本分块（500字符，50字符重叠）
4. LLM提取元数据（标题、作者、关键词）
5. 通过SiliconFlow API向量化文本块
6. 向量存储到向量数据库

### 问答流程
1. 用户提交问题
2. 问题向量化
3. 向量库搜索Top-K相似文本块
4. 从检索结果构建上下文
5. DeepSeek生成带上下文的答案
6. 答案和来源返回前端

## 关键设计决策

- **单例向量存储**: 上传和RAG引擎共享同一实例，确保数据一致性
- **批处理大小=1**: 防止向量化API的413错误
- **最大文本长度=512**: 截断长文本以兼容API
- **固定高度对话框**: 500px高度，内部滚动，提升用户体验
- **英文优先**: 所有提示词和响应使用英文，保持一致性

## 配置参数

- **分块大小**: 500字符
- **分块重叠**: 50字符
- **检索Top-K**: 3个文档
- **向量化模型**: BAAI/bge-large-zh-v1.5
- **大模型**: deepseek-chat
- **温度参数**: 0.7 (问答), 0.3 (元数据提取)



