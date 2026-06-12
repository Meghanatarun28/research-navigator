from research_navigator.retrieve.hybrid_retriever import (
    HybridRetriever,
)
from research_navigator.retrieve.retriever import (
    Retriever,
)


class ConfigComparison:
    def __init__(self):
        self.dense = Retriever()

        self.hybrid = HybridRetriever()

    def compare(
        self,
        query,
    ):
        dense_results = self.dense.search(
            query,
            limit=5,
        )

        hybrid_results = self.hybrid.search(
            query,
            limit=5,
        )

        return {
            "dense_count": len(dense_results),
            "hybrid_count": len(hybrid_results),
        }
