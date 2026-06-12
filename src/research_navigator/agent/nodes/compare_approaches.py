from research_navigator.retrieve.query_pipeline import (
    QueryPipeline,
)

pipeline = QueryPipeline()


def compare_approaches(
    state,
):
    query = state["query"]

    answer = "COMPARISON\n\n" + pipeline.answer(query)

    state["answer"] = answer

    return state
