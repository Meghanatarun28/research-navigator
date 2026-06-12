from research_navigator.evaluation.evaluator import (
    Evaluator,
)


def test_evaluator_creation():
    evaluator = Evaluator()

    assert evaluator is not None


def test_pipeline_exists():
    evaluator = Evaluator()

    assert evaluator.pipeline is not None
