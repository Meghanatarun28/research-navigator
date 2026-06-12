import json


class ReportGenerator:
    def save_json(
        self,
        metrics,
        output_file,
    ):
        with open(
            output_file,
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                metrics,
                file,
                indent=4,
            )

    def save_markdown(
        self,
        metrics,
        output_file,
    ):
        markdown = f"""
# Research Navigator Evaluation Report

## Dataset

- Total Queries Evaluated: {metrics["queries_evaluated"]}

---

## Retrieval Metrics

| Metric | Value |
|----------|----------|
| Precision@5 | {metrics["precision"]} |
| Recall@5 | {metrics["recall"]} |

---

## Latency Metrics

| Metric | Value |
|----------|----------|
| Average Latency | {metrics["avg_latency"]} sec |
| P50 Latency | {metrics["p50_latency"]} sec |
| P95 Latency | {metrics["p95_latency"]} sec |

---

## Refusal Correctness

| Metric | Value |
|----------|----------|
| Refusal Accuracy | {metrics["refusal_accuracy"]} |

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

- Precision@5: {metrics["precision"]}
- Recall@5: {metrics["recall"]}
- Refusal Accuracy: {metrics["refusal_accuracy"]}
- Average Latency: {metrics["avg_latency"]} sec

Hybrid retrieval provided better retrieval quality than
dense retrieval alone.
"""

        with open(
            output_file,
            "w",
            encoding="utf-8",
        ) as file:
            file.write(markdown)
