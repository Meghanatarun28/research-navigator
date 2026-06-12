from research_navigator.retrieve.citations import (
    CitationBuilder,
)
from research_navigator.retrieve.retriever import (
    Retriever,
)

retriever = Retriever()

results = retriever.search("What is a transformer?")

builder = CitationBuilder()

citations = builder.build(results)

for citation in citations:
    print()

    print(f"[{citation['number']}]")

    print(citation["title"])

    print(citation["authors"])

    print(citation["year"])

    print(citation["section"])

    print(citation["url"])
