from research_navigator.evaluation.metrics import (
    precision_at_k,
    recall_at_k,
)


def test_empty_metrics():
    assert (
        precision_at_k(
            [],
            [],
            5,
        )
        == 0
    )

    assert (
        recall_at_k(
            [],
            [],
            5,
        )
        == 0
    )
