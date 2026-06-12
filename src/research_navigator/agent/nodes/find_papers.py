# find_papers.py

from research_navigator.retrieve.query_pipeline import (
    QueryPipeline,
)

pipeline = QueryPipeline()


def find_papers(state):
    answer = pipeline.answer(state["query"])

    state["answer"] = "RECOMMENDED PAPERS\n\n" + answer

    return state
