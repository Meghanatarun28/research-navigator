def route_query(state):
    query = state["query"].lower()

    if "compare" in query:
        route = "compare_approaches"

    elif "paper" in query or "attention is all you need" in query:
        route = "paper_deep_dive"

    elif "recent" in query or "latest" in query:
        route = "recent_developments"

    elif "find papers" in query or "recommend papers" in query:
        route = "find_papers"

    elif "weather" in query or "cricket" in query:
        route = "fallback"

    else:
        route = "concept_explanation"

    state["route"] = route

    return state
