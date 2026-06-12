from research_navigator.retrieve.bm25_retriever import (
    BM25Retriever,
)

retriever = BM25Retriever()

results = retriever.search("transformer architecture")

for point, score in results:
    print()

    print(f"Score: {score:.4f}")

    print(point.payload["title"])

    print(point.payload["year"])
