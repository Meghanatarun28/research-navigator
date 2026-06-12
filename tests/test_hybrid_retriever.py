from research_navigator.retrieve.hybrid_retriever import (
    HybridRetriever,
)


def test_hybrid_creation():
    retriever = HybridRetriever()

    assert retriever is not None


def test_components_exist():
    retriever = HybridRetriever()

    assert retriever.dense is not None
    assert retriever.bm25 is not None
