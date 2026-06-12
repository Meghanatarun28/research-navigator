from unittest.mock import Mock

from research_navigator.evaluation.refusal_evaluator import (
    RefusalEvaluator,
)


def test_not_refused():
    evaluator = RefusalEvaluator()

    evaluator.pipeline.retriever.search = Mock(return_value=[{"score": 0.95}])

    result = evaluator.evaluate(["question"])

    assert result["correct_refusals"] == 0
