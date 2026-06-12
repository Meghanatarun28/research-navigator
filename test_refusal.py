import json

from research_navigator.evaluation.refusal_evaluator import (
    RefusalEvaluator,
)

with open(
    "src/research_navigator/evaluation/refusal_questions.json",
    encoding="utf-8",
) as file:
    questions = json.load(file)

evaluator = RefusalEvaluator()

result = evaluator.evaluate(questions)

print()

print("=" * 60)

print(f"Refusal Accuracy: {round(result['accuracy'], 3)}")

print(f"Correct Refusals: {result['correct_refusals']}")

print(f"Total Questions: {result['total_questions']}")

print("=" * 60)
