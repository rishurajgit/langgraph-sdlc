from langgraph.graph import START, END, StateGraph

from app.state.state import SDLCState
from app.nodes.requirements import user_requirements_node
from app.nodes.user_story import generate_user_story_node

builder = StateGraph(SDLCState)

builder.add_node("requirements", user_requirements_node)
builder.add_node("user_story", generate_user_story_node)

builder.add_edge(START, "requirements")
builder.add_edge("requirements", "user_story")
builder.add_edge("user_story", END)

graph = builder.compile()