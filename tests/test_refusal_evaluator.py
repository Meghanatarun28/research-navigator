from research_navigator.evaluation.refusal_evaluator import (
    RefusalEvaluator,
)


def test_refusal_creation():
    evaluator = RefusalEvaluator()

    assert evaluator is not None


def test_threshold():
    evaluator = RefusalEvaluator()

    assert evaluator.THRESHOLD == 0.70
