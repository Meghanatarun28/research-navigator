from research_navigator.retrieve.hybrid_retriever import (
    HybridRetriever,
)

retriever = HybridRetriever()

results = retriever.search("transformer architecture")

for rank, result in enumerate(
    results,
    start=1,
):
    point = result["point"]

    print()

    print(f"Rank {rank}")

    print(f"Fusion Score: {result['score']:.4f}")

    print(point.payload["title"])

    print(point.payload["year"])

    print(point.payload["section_title"])

    print(point.payload["text"][:300])
