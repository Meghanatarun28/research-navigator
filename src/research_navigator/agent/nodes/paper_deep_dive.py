from research_navigator.retrieve.query_pipeline import (
    QueryPipeline,
)

pipeline = QueryPipeline()


def paper_deep_dive(
    state,
):
    query = state["query"]

    answer = "PAPER DEEP DIVE\n\n" + pipeline.answer(query)

    state["answer"] = answer

    return state
