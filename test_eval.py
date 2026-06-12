import time

from research_navigator.retrieve.query_pipeline import (
    QueryPipeline,
)

pipeline = QueryPipeline()

with open(
    "tests/eval_questions.txt",
    encoding="utf-8",
) as file:
    questions = [q.strip() for q in file if q.strip()]
    print(f"Loaded {len(questions)} questions")

for index, question in enumerate(
    questions,
    start=1,
):
    print("\n" + "=" * 80)

    print(f"Question {index}")

    print(question)

    print()

    answer = pipeline.answer(question)

    print(answer)
    time.sleep(15)
