from research_navigator.agent.graph import (
    graph,
)

result = graph.invoke(
    {
        "query": "Recent developments in RAG",
        "route": "",
        "answer": "",
        "filters": {},
        "papers": [],
    }
)

print(result)
