from langgraph.graph import START, END, StateGraph

from app.state.state import SDLCState
from app.nodes.requirements import user_requirements_node
from app.nodes.user_story import generate_user_story_node
from app.nodes.product_owner_review import product_owner_review_node
from app.nodes.revise_user_story import revise_user_story_node
from app.nodes.design import design_node
from app.nodes.design_review import design_review_node
from app.nodes.revise_design import revise_design_node



builder = StateGraph(SDLCState)

#Register Nodes

builder.add_node("requirements", user_requirements_node)
builder.add_node("user_story", generate_user_story_node)

builder.add_node("review", product_owner_review_node)
builder.add_node("revise_story", revise_user_story_node)

builder.add_node("design", design_node)
builder.add_node("design_review", design_review_node)
builder.add_node("revise_design", revise_design_node)


#Basic Flow

builder.add_edge(START, "requirements")
builder.add_edge("requirements", "user_story")
builder.add_edge("user_story", "review")

#Product Owner Review

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


#Design Review

builder.add_edge("design", "design_review")

def design_review_router(state: SDLCState):
    if state["design_review_status"] == "approved":
        return END
    
    return "revise_design"

builder.add_conditional_edges(
    "design_review",
    design_review_router,
    {
        END: END,
        "revise_design": "revise_design"
    }
)

# builder.add_edge("design", END)
builder.add_edge("revise_design", "design_review")


graph = builder.compile()