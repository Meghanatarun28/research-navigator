from datetime import datetime


def recent_developments(
    state,
):
    current_year = datetime.now().year

    state["filters"] = {"year_gte": current_year - 1}

    state["answer"] = (
        f"Recent developments route. Applying filter: year >= {current_year - 1}"
    )

    return state
