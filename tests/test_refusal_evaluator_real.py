from unittest.mock import Mock

from research_navigator.evaluation.refusal_evaluator import (
    RefusalEvaluator,
)


def test_refusal_when_no_results():
    evaluator = RefusalEvaluator()

    evaluator.pipeline.retriever.search = Mock(return_value=[])

    result = evaluator.evaluate(["question"])

    assert result["correct_refusals"] == 1
