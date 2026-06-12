from research_navigator.retrieve.query_pipeline import (
    QueryPipeline,
)

pipeline = QueryPipeline()

print(pipeline.answer("What is a transformer?"))

print()

print(pipeline.answer("How do cats build quantum computers?"))
