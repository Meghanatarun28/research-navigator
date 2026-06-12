from research_navigator.retrieve.query_understanding import (
    QueryUnderstanding,
)
from research_navigator.retrieve.retriever import (
    Retriever,
)

query = "recent transformer papers"

understanding = QueryUnderstanding()

filters = understanding.extract_filters(query)

print("Extracted Filters:")
print(filters)

retriever = Retriever()

results = retriever.search(
    query,
    filters=filters,
)

retriever.pretty_print(results)
