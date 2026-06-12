from research_navigator.retrieve.hybrid_retriever import (
    HybridRetriever,
)


def test_hybrid_constants():
    retriever = HybridRetriever()

    assert retriever is not None


def test_has_components():
    retriever = HybridRetriever()

    assert retriever.dense is not None
    assert retriever.bm25 is not None
