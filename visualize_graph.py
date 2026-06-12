from research_navigator.agent.graph import (
    graph,
)

png = graph.get_graph().draw_mermaid_png()

with open(
    "m3_graph.png",
    "wb",
) as file:
    file.write(png)

print("Graph saved as m3_graph.png")
