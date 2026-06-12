from langgraph.graph import (
    END,
    StateGraph,
)

from research_navigator.agent.nodes.compare_approaches import (
    compare_approaches,
)
from research_navigator.agent.nodes.concept_explanation import (
    concept_explanation,
)
from research_navigator.agent.nodes.fallback import (
    fallback,
)
from research_navigator.agent.nodes.find_papers import (
    find_papers,
)
from research_navigator.agent.nodes.paper_deep_dive import (
    paper_deep_dive,
)
from research_navigator.agent.nodes.recent_developments import (
    recent_developments,
)
from research_navigator.agent.router import (
    route_query,
)
from research_navigator.agent.state import (
    AgentState,
)

builder = StateGraph(AgentState)

# -----------------------
# Nodes
# -----------------------

builder.add_node(
    "router",
    route_query,
)

builder.add_node(
    "concept_explanation",
    concept_explanation,
)

builder.add_node(
    "paper_deep_dive",
    paper_deep_dive,
)

builder.add_node(
    "compare_approaches",
    compare_approaches,
)

builder.add_node(
    "recent_developments",
    recent_developments,
)

builder.add_node(
    "find_papers",
    find_papers,
)

builder.add_node(
    "fallback",
    fallback,
)

# -----------------------
# Entry Point
# -----------------------

builder.set_entry_point("router")

# -----------------------
# Router Logic
# -----------------------

builder.add_conditional_edges(
    "router",
    lambda state: state["route"],
    {
        "concept_explanation": "concept_explanation",
        "paper_deep_dive": "paper_deep_dive",
        "compare_approaches": "compare_approaches",
        "recent_developments": "recent_developments",
        "find_papers": "find_papers",
        "fallback": "fallback",
    },
)

# -----------------------
# End Nodes
# -----------------------

builder.add_edge(
    "concept_explanation",
    END,
)

builder.add_edge(
    "paper_deep_dive",
    END,
)

builder.add_edge(
    "compare_approaches",
    END,
)

builder.add_edge(
    "recent_developments",
    END,
)

builder.add_edge(
    "find_papers",
    END,
)

builder.add_edge(
    "fallback",
    END,
)

# -----------------------
# Compile Graph
# -----------------------

graph = builder.compile()
