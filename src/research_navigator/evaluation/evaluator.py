import json
import time

from research_navigator.evaluation.metrics import (
    precision_at_k,
    recall_at_k,
)
from research_navigator.retrieve.query_pipeline import (
    QueryPipeline,
)


class Evaluator:
    def __init__(self):
        self.pipeline = QueryPipeline()

    def evaluate(
        self,
        golden_set_path,
    ):
        with open(
            golden_set_path,
            encoding="utf-8",
        ) as file:
            golden_set = json.load(file)

        results = []

        for item in golden_set:
            query = item["question"]

            expected_sources = item["expected_sources"]

            start_time = time.time()

            retrieved = self.pipeline.retriever.search(
                query,
                limit=5,
            )

            latency = time.time() - start_time

            retrieved_titles = []

            for result in retrieved:
                point = result["point"]

                title = point.payload.get("title", "")

                retrieved_titles.append(title)

            precision = precision_at_k(
                retrieved_titles,
                expected_sources,
                k=5,
            )

            recall = recall_at_k(
                retrieved_titles,
                expected_sources,
                k=5,
            )

            results.append(
                {
                    "query": query,
                    "precision": precision,
                    "recall": recall,
                    "latency": latency,
                }
            )

        return results
