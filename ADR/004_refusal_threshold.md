# ADR 004: Refusal Threshold

## Status

Accepted

## Context

The system should avoid answering questions unsupported by the corpus.

## Decision

Use a retrieval confidence threshold of 0.70.

## Rationale

Balances answer coverage and hallucination prevention.

## Consequences

Some borderline queries may be refused, but unsupported answers are reduced.
