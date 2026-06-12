# M3 Agentic Layer Design

## Architecture

Router
→ ConceptExplanation
→ PaperDeepDive
→ CompareApproaches
→ RecentDevelopments
→ FindPapers
→ Fallback

## State

AgentState

Fields:

- query
- route
- answer
- filters
- papers

## Tool Usage

RecentDevelopments uses datetime to apply
recency filtering.

Example:

year >= current_year - 1

## Retrieval

Uses M2 Hybrid Retrieval:

- Dense Retrieval
- BM25 Retrieval
- Hybrid Fusion

## Output

All routes return serialized AgentState.