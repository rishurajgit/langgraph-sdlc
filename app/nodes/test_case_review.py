from app.state.state import SDLCState
from app.services.llm import invoke_llm


def test_case_review_node(state: SDLCState):
    attempts = state["test_review_attempts"] + 1
    

    prompt = f"""
You are a Senior QA Engineer.

Review these test cases.

Test Cases:

{state["test_cases"]}

Evaluate only:

- Coverage
- Clarity

Rules:

If acceptable reply exactly:

STATUS: approved

Feedback:
None

- Return STATUS: feedback ONLY if important test cases are missing.

STATUS: feedback

Feedback:
<max 20 words>

Do not rewrite the test cases.
"""

    review = invoke_llm(prompt)

    print("\n======= TEST CASE REVIEW =======\n")
    print(review)

    if "STATUS: APPROVED" in review.upper():
        return {
            "test_review_status": "approved",
            "test_feedback": "",
            "test_review_attempts": attempts
        }

    feedback = ""

    if "FEEDBACK:" in review.upper():
        feedback = review.split("Feedback:", 1)[-1].strip()

    return {
        "test_review_status": "feedback",
        "test_feedback": feedback,
        "test_review_attempts": attempts
    }