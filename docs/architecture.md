# Research Navigator Architecture

## System Overview

Research Navigator is a Retrieval-Augmented Generation (RAG) system designed for exploring AI research papers.

## Architecture Flow

Research Papers

↓

Document Parsing

↓

Chunking

↓

Embeddings (BAAI/bge-small-en-v1.5)

↓

Qdrant Vector Database

↓

Hybrid Retrieval

* Dense Retrieval
* BM25 Retrieval
* Score Fusion

↓

LangGraph Router

* Concept Explanation
* Paper Deep Dive
* Compare Approaches
* Recent Developments

↓

Answer Generation (Qwen3:8B)

↓

Citations

↓

Final Response

## Components

### Ingestion Layer

Responsible for:

* Parsing PDFs
* Extracting metadata
* Chunk generation
* Embedding creation
* Storage in Qdrant

### Retrieval Layer

Responsible for:

* Semantic retrieval
* BM25 retrieval
* Hybrid ranking
* Metadata filtering

### Agent Layer

Responsible for:

* Query routing
* Specialized workflows
* LangGraph execution

### Evaluation Layer

Responsible for:

* Precision@5
* Recall@5
* Refusal accuracy
* Latency measurement

## Storage

Qdrant is used as the vector database.

## Models

Embedding Model:
BAAI/bge-small-en-v1.5

Generation Model:
Qwen3:8B
