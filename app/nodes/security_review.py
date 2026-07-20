from app.services.llm import invoke_llm
from app.state.state import SDLCState


def security_review_node(state: SDLCState):
    attempts = state["security_review_attempts"] + 1

    prompt = f"""
You are a Security Reviewer.

Review this project skeleton.

{state["generated_code"]}

Review ONLY:
- Folder structure
- Security architecture
- Auth module presence
- API security design

Ignore:
- Missing implementation
- Missing CRUD
- Missing business logic

Rules:
- Minor suggestions -> STATUS: approved
- Major security issue -> STATUS: feedback

Reply ONLY:

STATUS: approved
Feedback: None

OR

STATUS: feedback
Feedback: <max 30 words>
"""

    review = invoke_llm(prompt)

    print("\n======= SECURITY REVIEW =======\n")
    print(review)

    if "STATUS: APPROVED" in review.upper():
        return {
            "security_review_status": "approved",
            "security_feedback": ""
        }

    feedback = ""

    if "FEEDBACK:" in review.upper():
        feedback = review.split("Feedback:", 1)[-1].strip()

    return {
        "security_review_status": "feedback",
        "security_feedback": feedback
    }