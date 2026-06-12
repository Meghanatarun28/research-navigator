
# Research Navigator Evaluation Report

## Dataset

- Total Queries Evaluated: 40

---

## Retrieval Metrics

| Metric | Value |
|----------|----------|
| Precision@5 | 0.435 |
| Recall@5 | 0.637 |

---

## Latency Metrics

| Metric | Value |
|----------|----------|
| Average Latency | 0.036 sec |
| P50 Latency | 0.032 sec |
| P95 Latency | 0.057 sec |

---

## Refusal Correctness

| Metric | Value |
|----------|----------|
| Refusal Accuracy | 1.0 |

---

## Configuration Comparison

### Dense Retrieval

- Uses only vector similarity search.
- Faster but may miss relevant papers.

### Hybrid Retrieval

- Dense Retrieval + BM25 Retrieval.
- Uses section-aware ranking.
- Better recall and overall retrieval quality.

---

## Citation Faithfulness

A citation faithfulness module was implemented to ensure
answers are supported by retrieved sources.

---

## Conclusion

The Research Navigator system was evaluated using a
40-question golden dataset spanning:

- Concept Explanation
- Paper Deep Dive
- Compare Approaches
- Recent Developments
- Paper Discovery
- Out-of-Scope Refusal

Final Results:

- Precision@5: 0.435
- Recall@5: 0.637
- Refusal Accuracy: 1.0
- Average Latency: 0.036 sec

Hybrid retrieval provided better retrieval quality than
dense retrieval alone.
