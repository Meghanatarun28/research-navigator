from research_navigator.evaluation.metrics import (
    recall_at_k,
)


def test_recall():
    retrieved = [
        "A",
        "B",
        "C",
    ]

    expected = [
        "A",
        "B",
    ]

    score = recall_at_k(
        retrieved,
        expected,
        k=3,
    )

    assert score == 1.0
