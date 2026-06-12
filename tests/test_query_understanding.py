from research_navigator.retrieve.query_understanding import (
    QueryUnderstanding,
)


def test_recent_filter():
    parser = QueryUnderstanding()

    filters = parser.extract_filters("recent papers")

    assert filters["year_gte"] == 2023


def test_non_recent_query():
    parser = QueryUnderstanding()

    filters = parser.extract_filters("papers about transformers")

    assert filters == {}
