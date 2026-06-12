from research_navigator.retrieve.query_pipeline import (
    QueryPipeline,
)

pipeline = QueryPipeline()


def concept_explanation(
    state,
):
    answer = pipeline.answer(state["query"])

    state["answer"] = answer

    return state
