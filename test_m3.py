from research_navigator.agent.graph import (
    graph,
)

queries = [
    "What is a transformer?",
    "Explain Attention Is All You Need paper",
    "Compare BERT vs GPT-3",
    "Recent developments in RAG",
    "Find papers about transformers",
    "What is today's weather?",
]

for query in queries:
    print("\n" + "=" * 80)

    print(query)

    result = graph.invoke(
        {
            "query": query,
            "route": "",
            "answer": "",
            "filters": {},
            "papers": [],
        }
    )

    print(result["answer"])
