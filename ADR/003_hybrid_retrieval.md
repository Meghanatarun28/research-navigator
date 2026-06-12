# ADR 003: Hybrid Retrieval

## Status

Accepted

## Context

Dense retrieval alone may miss exact keyword matches.

## Decision

Use Hybrid Retrieval:

* Dense Vector Search
* BM25 Search
* Weighted Fusion

## Rationale

Combines semantic similarity with lexical matching.

## Consequences

Higher retrieval recall and better robustness.
