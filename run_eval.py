from research_navigator.evaluation.evaluator import (
    Evaluator,
)

evaluator = Evaluator()

report = evaluator.evaluate("src/research_navigator/evaluation/golden_set.json")

for result in report["details"]:
    print()

    print(f"Query: {result['question']}")

    print(f"Precision: {round(result['precision'], 3)}")

    print(f"Recall: {round(result['recall'], 3)}")

print()

print("=" * 60)

print(f"Queries Evaluated: {len(report['details'])}")

print(f"Average Precision@5: {round(report['precision_at_5'], 3)}")

print(f"Average Recall@5: {round(report['recall_at_5'], 3)}")

print(f"Average Latency: {round(report['average_latency'], 3)} sec")

print(f"P50 Latency: {round(report['p50_latency'], 3)} sec")

print(f"P95 Latency: {round(report['p95_latency'], 3)} sec")
