from langgraph.graph import START, END, StateGraph

from app.state.state import SDLCState
from app.nodes.requirements import user_requirements_node
from app.nodes.user_story import generate_user_story_node
from app.nodes.product_owner_review import product_owner_review_node
from app.nodes.revise_user_story import revise_user_story_node
from app.nodes. design import design_node

builder = StateGraph(SDLCState)

builder.add_node("requirements", user_requirements_node)
builder.add_node("user_story", generate_user_story_node)
builder.add_node("review", product_owner_review_node)
builder.add_node("revise_story", revise_user_story_node)
builder.add_node("design", design_node)



builder.add_edge(START, "requirements")
builder.add_edge("requirements", "user_story")
builder.add_edge("user_story", "review")

def review_router(state: SDLCState):
    
    if state["review_status"] == "approved":
        return "design"
    return "revise_story"


builder.add_conditional_edges(
    "review",
    review_router,
    {
        "design": "design",
        "revise_story": "revise_story",
    },
)


builder.add_edge("revise_story", "review")

builder.add_edge("design", END)



graph = builder.compile()