from typing import TypedDict

class PortfolioState(TypedDict):
    amt_usd: float
    total_usd: float
    total_inr : float

def calc_total(state:PortfolioState)->PortfolioState:
    state['total_usd'] = state['amt_usd'] * 1.80
    return state

def convert_to_inr(state:PortfolioState)->PortfolioState:
    state['total_inr'] = state['total_usd'] * 0.80
    return state

from langgraph.graph import StateGraph,START,END

graph = StateGraph(PortfolioState)

graph.add_node("calc_total", calc_total)
graph.add_node("convert_to_inr",convert_to_inr)

graph.add_edge(START,"calc_total")
graph.add_edge("calc_total","convert_to_inr")
graph.add_edge("convert_to_inr",END)

graph_actual = graph.compile()

from IPython.display import Image, display

display(Image(graph_actual.get_graph().draw_mermaid_png()))