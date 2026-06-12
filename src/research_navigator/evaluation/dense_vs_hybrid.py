from research_navigator.evaluation.metrics import (
    precision_at_k,
    recall_at_k,
)
from research_navigator.retrieve.hybrid_retriever import (
    HybridRetriever,
)
from research_navigator.retrieve.retriever import (
    Retriever,
)


class DenseVsHybrid:
    def __init__(self):
        self.dense = Retriever()

        self.hybrid = HybridRetriever()

    def compare(
        self,
        query,
        expected_sources,
    ):
        dense_results = self.dense.search(
            query,
            limit=5,
        )

        hybrid_results = self.hybrid.search(
            query,
            limit=5,
        )

        dense_titles = [
            point.payload.get(
                "title",
                "",
            )
            for point in dense_results
        ]

        hybrid_titles = [
            result["point"].payload.get(
                "title",
                "",
            )
            for result in hybrid_results
        ]

        return {
            "dense_precision": precision_at_k(
                dense_titles,
                expected_sources,
                5,
            ),
            "dense_recall": recall_at_k(
                dense_titles,
                expected_sources,
                5,
            ),
            "hybrid_precision": precision_at_k(
                hybrid_titles,
                expected_sources,
                5,
            ),
            "hybrid_recall": recall_at_k(
                hybrid_titles,
                expected_sources,
                5,
            ),
        }
