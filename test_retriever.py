from research_navigator.retrieve.retriever import (
    Retriever,
)

retriever = Retriever()

results = retriever.search("What is a transformer?")

retriever.pretty_print(results)
