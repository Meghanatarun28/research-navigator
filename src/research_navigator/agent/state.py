from typing import TypedDict


class AgentState(TypedDict):
    query: str

    route: str

    answer: str

    filters: dict

    papers: list
