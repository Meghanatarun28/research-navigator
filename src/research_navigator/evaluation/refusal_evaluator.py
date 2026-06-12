from research_navigator.retrieve.query_pipeline import (
    QueryPipeline,
)


class RefusalEvaluator:
    THRESHOLD = 0.70

    def __init__(self):
        self.pipeline = QueryPipeline()

    def evaluate(
        self,
        questions,
    ):
        correct_refusals = 0

        for question in questions:
            results = self.pipeline.retriever.search(
                question,
                limit=5,
            )

            refused = False

            if not results:
                refused = True

                print(f"{question} -> REFUSED (No Results)")

            else:
                best_score = results[0]["score"]

                print(f"{question} -> Score: {round(best_score, 4)}")

                if best_score < self.THRESHOLD:
                    refused = True

                    print("REFUSED")

                else:
                    print("NOT REFUSED")

            if refused:
                correct_refusals += 1

        accuracy = correct_refusals / len(questions)

        return {
            "total_questions": len(questions),
            "correct_refusals": correct_refusals,
            "accuracy": accuracy,
        }
