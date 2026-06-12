from unittest.mock import Mock

from research_navigator.retrieve.query_pipeline import (
    QueryPipeline,
)


def test_pipeline_no_results():
    pipeline = QueryPipeline()

    pipeline.retriever.search = Mock(return_value=[])

    answer = pipeline.answer("test")

    assert "don't have enough" in answer.lower()
