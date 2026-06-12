from research_navigator.retrieve.query_pipeline import (
    QueryPipeline,
)


def test_pipeline_components():
    pipeline = QueryPipeline()

    assert pipeline.retriever is not None
    assert pipeline.query_understanding is not None
    assert pipeline.citation_builder is not None
    assert pipeline.answer_generator is not None


def test_pipeline_threshold():
    pipeline = QueryPipeline()

    assert pipeline.MIN_SCORE == 0.40
