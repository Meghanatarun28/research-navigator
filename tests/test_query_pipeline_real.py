from unittest.mock import Mock

from research_navigator.retrieve.query_pipeline import (
    QueryPipeline,
)


def test_no_results_refusal():
    pipeline = QueryPipeline()

    pipeline.retriever.search = Mock(return_value=[])

    answer = pipeline.answer("test query")

    assert "don't have enough" in answer.lower()
