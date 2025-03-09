from IPython.display import Image, display
from langgraph.graph.state import CompiledStateGraph

def display_graph(graph: CompiledStateGraph):
    display(Image(graph.get_graph().draw_mermaid_png()))