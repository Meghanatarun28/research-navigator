# Research Navigator

## Overview

Research Navigator is a Retrieval-Augmented Generation (RAG) system for exploring AI research papers.

Features:

* Research paper ingestion
* Semantic search
* Hybrid retrieval (Dense + BM25)
* LangGraph agent routing
* Citation generation
* Refusal handling
* Evaluation framework

---

## Project Structure

```text
src/research_navigator

├── ingest/
├── retrieve/
├── agent/
├── evaluation/
├── config/
```

---

## Setup

### Create Environment

```bash
uv sync
```

### Start Services

```bash
docker compose up
```

### Run Ingestion

```bash
python test_ingest.py
```

### Run Retrieval

```bash
python test_query_pipeline.py
```

### Run Evaluation

```bash
python src/research_navigator/evaluation/evaluation_runner.py
```

---

## Evaluation Results

* Precision@5: 0.435
* Recall@5: 0.637
* Refusal Accuracy: 1.0

---

## Technologies

* Python
* Qdrant
* LangGraph
* Ollama
* Qwen3
* SentenceTransformers
