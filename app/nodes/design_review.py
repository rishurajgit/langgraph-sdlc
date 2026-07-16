from app.state.state import SDLCState

def design_review_node(state: SDLCState):
    print("\n========DESIGN REVIEW======\n")
    
    print(state["design_doc"])
    
    decision = input(
        "\n Approve Design? (approved / feedback):"
    ).strip().lower()
    
    if decision == "approved":
        return{
            "design_review_status": "approved",
            "design_feedback": ""
        }
        
    feedback = input("Enter Design Feedback:")
    return{
        "design_review_status": "feedback",
        "design_feedback": feedback
    }