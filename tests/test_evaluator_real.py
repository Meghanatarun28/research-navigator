import json
from unittest.mock import Mock

from research_navigator.evaluation.evaluator import (
    Evaluator,
)


def test_evaluate_runs(
    tmp_path,
):
    data = [
        {
            "question": "What is BERT?",
            "expected_sources": ["BERT"],
        }
    ]

    file = tmp_path / "golden.json"

    file.write_text(
        json.dumps(data),
        encoding="utf-8",
    )

    evaluator = Evaluator()

    fake_point = Mock()

    fake_point.payload = {"title": "BERT"}

    evaluator.pipeline.retriever.search = Mock(return_value=[{"point": fake_point}])

    results = evaluator.evaluate(str(file))

    assert len(results) == 1
