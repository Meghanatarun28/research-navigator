# ADR 001: Embedding Model Selection

## Status

Accepted

## Context

The Research Navigator requires a lightweight embedding model for semantic retrieval over AI research papers.

## Decision

Use BAAI/bge-small-en-v1.5 as the embedding model.

## Rationale

* Strong retrieval performance
* Small memory footprint
* Fast inference
* Compatible with Qdrant

## Consequences

Improved retrieval speed while maintaining acceptable semantic search quality.
