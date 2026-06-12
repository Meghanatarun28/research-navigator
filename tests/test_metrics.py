from research_navigator.evaluation.metrics import (
    precision_at_k,
)


def test_precision():
    retrieved = [
        "A",
        "B",
        "C",
    ]

    expected = [
        "A",
        "B",
    ]

    score = precision_at_k(
        retrieved,
        expected,
        k=3,
    )

    assert score > 0
