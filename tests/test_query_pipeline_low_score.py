from unittest.mock import Mock

from research_navigator.retrieve.query_pipeline import (
    QueryPipeline,
)


def test_pipeline_low_score():
    pipeline = QueryPipeline()

    pipeline.retriever.search = Mock(
        return_value=[
            {
                "score": 0.1,
                "point": Mock(),
            }
        ]
    )

    answer = pipeline.answer("test")

    assert "don't have enough" in answer.lower()
