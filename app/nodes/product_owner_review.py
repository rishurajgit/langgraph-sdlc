from app.state.state import SDLCState


def product_owner_review_node(state: SDLCState):

    story = state["user_stories"]

    print("\n===== PRODUCT OWNER REVIEW =====")
    print(story)

    decision = input(
        "\nApprove user story? (approved / feedback): "
    ).strip().lower()

    if decision == "approved":
        return {
            "review_status": "approved",
            "feedback": ""
        }

    feedback = input("Enter feedback: ")

    return {
        "review_status": "feedback",
        "feedback": feedback
    }