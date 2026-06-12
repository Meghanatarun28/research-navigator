# ADR 002: Chunking Strategy

## Status

Accepted

## Context

Research papers are large documents and cannot be embedded as a single unit.

## Decision

Chunk papers by section and text length.

## Rationale

* Preserves semantic coherence
* Improves retrieval precision
* Enables citation generation at chunk level

## Consequences

More chunks are stored, but retrieval quality improves significantly.
