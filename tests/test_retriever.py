from research_navigator.retrieve.retriever import (
    Retriever,
)


def test_year_filter_exists():
    retriever = Retriever()

    result = retriever.build_filter(
        {
            "year_gte": 2024,
        }
    )

    assert result is not None


def test_tags_filter_exists():
    retriever = Retriever()

    result = retriever.build_filter(
        {
            "tags": [
                "llm",
                "rag",
            ]
        }
    )

    assert result is not None


def test_combined_filter():
    retriever = Retriever()

    result = retriever.build_filter(
        {
            "year_gte": 2024,
            "tags": ["llm"],
        }
    )

    assert result is not None
