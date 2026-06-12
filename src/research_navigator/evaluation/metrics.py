def precision_at_k(
    retrieved_sources,
    expected_sources,
    k=5,
):
    retrieved = set(retrieved_sources[:k])

    expected = set(expected_sources)

    if not retrieved:
        return 0.0

    return len(retrieved.intersection(expected)) / len(retrieved)


def recall_at_k(
    retrieved_sources,
    expected_sources,
    k=5,
):
    retrieved = set(retrieved_sources[:k])

    expected = set(expected_sources)

    if not expected:
        return 0.0

    return len(retrieved.intersection(expected)) / len(expected)
