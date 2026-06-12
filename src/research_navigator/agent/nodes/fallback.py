# fallback.py


def fallback(state):
    state["answer"] = "Sorry, this query is outside the scope of Research Navigator."

    return state
