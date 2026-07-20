from langgraph.graph import START, END, StateGraph

from app.state.state import SDLCState
from app.nodes.requirements import user_requirements_node
from app.nodes.user_story import generate_user_story_node
from app.nodes.product_owner_review import product_owner_review_node
from app.nodes.revise_user_story import revise_user_story_node
from app.nodes.design import design_node
from app.nodes.design_review import design_review_node
from app.nodes.revise_design import revise_design_node
from app.nodes.code_generation import code_generation_node
from app.nodes.code_review import code_review_node
from app.nodes.revise_code import revise_code_node
from app.nodes.security_review import security_review_node
from app.nodes.fix_security import fix_security_node
from app.nodes.generate_test_cases import generate_test_cases_node
from app.nodes.test_case_review import test_case_review_node
from app.nodes.revise_test_cases import revise_test_cases_node
from app.nodes.qa_testing import qa_testing_node
from app.nodes.deployment import deployment_node

from app.checkpoint.sqlite_checkpointer import checkpointer

builder = StateGraph(SDLCState)

#Register Nodes

builder.add_node("requirements", user_requirements_node)
builder.add_node("user_story", generate_user_story_node)

builder.add_node("review", product_owner_review_node)
builder.add_node("revise_story", revise_user_story_node)

builder.add_node("design", design_node)
builder.add_node("design_review", design_review_node)
builder.add_node("revise_design", revise_design_node)

builder.add_node("generate_code", code_generation_node)

builder.add_node("code_review", code_review_node)
builder.add_node("revise_code", revise_code_node)

builder.add_node("security_review", security_review_node)
builder.add_node("fix_security", fix_security_node)

builder.add_node("generate_test_cases", generate_test_cases_node)
builder.add_node("test_case_review", test_case_review_node)
builder.add_node("revise_test_cases", revise_test_cases_node)

builder.add_node("qa_testing", qa_testing_node)

builder.add_node("deployment", deployment_node)


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

builder.add_edge("revise_story", "review")
#Design Review

builder.add_edge("design", "design_review")

def design_review_router(state: SDLCState):
    if state["design_review_status"] == "approved":
        return "generate_code"
    
    return "revise_design"

builder.add_conditional_edges(
    "design_review",
    design_review_router,
    {
        # END: END,
        "revise_design": "revise_design",
        "generate_code": "generate_code"
    }
)

# builder.add_edge("design", END)
builder.add_edge("revise_design", "design_review")
# builder.add_edge("generate_code", END)
builder.add_edge("generate_code", "code_review")

#code review
def code_review_router(state: SDLCState):
    
    if state["code_review_status"] == "approved":
        # return END
        return "security_review"
    
    if state["code_review_attempts"] >=2:
        print("\nMaximum code review attempts reached.")
        print("Proceeding with current code.\n")
        return "security_review"

    return "revise_code"


builder.add_conditional_edges(
    "code_review",
    code_review_router,
    {
        # END: END,
        "security_review": "security_review",
        "revise_code": "revise_code",
    },
)

builder.add_edge("revise_code", "code_review")

# Security review

def security_review_router(state: SDLCState):
    
    if state["security_review_status"] == "approved":
        # return END
        return "generate_test_cases"
    
    
    if state["security_review_attempts"] >= 2:
        print("\nMaximum security review attempts reached.")
        print("Proceeding with current security design.\n")
        return "generate_test_cases"

    return "fix_security"

builder.add_conditional_edges(
    "security_review",
    security_review_router,
    {
        # END: END,
        "generate_test_cases": "generate_test_cases",
        "fix_security": "fix_security",
    }
)
builder.add_edge("fix_security", "security_review")
# builder.add_edge("generate_test_cases", END)
builder.add_edge("generate_test_cases", "test_case_review")

def test_case_review_router(state: SDLCState):
    if state["test_review_status"] == "approved":
        # return END
        return "qa_testing"
    
    if state["test_review_attempts"] >=2:
        print("\nMaximum review attempts reached.")
        print("Proceeding with current test cases.\n")
        return "qa_testing"
    
    return "revise_test_cases"

# builder.add_conditional_edges(
#     "test_case_review",
#     test_case_review_router,
#     {
#         END: END,
#         "revise_test_cases": "revise_test_cases",
#     },
# )
builder.add_conditional_edges(
    "test_case_review",
    test_case_review_router,
    {
        "qa_testing": "qa_testing",
        "revise_test_cases": "revise_test_cases",
    },
)

builder.add_edge(
    "revise_test_cases",
    "test_case_review"
)

# builder.add_edge("qa_testing", END)
def qa_testing_router(state: SDLCState):
    
    if state["qa_status"] == "PASS":
        return "deployment"
    
    if state["qa_attempts"] >= 2:
        print("\nMaximum QA attempts reached.")
        print("Ending workflow.\n")
        return "deployment"

    return "generate_code"

builder.add_conditional_edges(
    "qa_testing",
    qa_testing_router,
    {
        # END: END,
        "deployment": "deployment",
        "generate_code": "generate_code",
    },
)

builder.add_edge("deployment", END)

graph = builder.compile(
    checkpointer= checkpointer
)