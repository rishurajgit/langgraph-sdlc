from app.services.llm import invoke_llm
from app.state.state import SDLCState


def revise_test_cases_node(state: SDLCState):

    prompt = f"""
You are a Senior QA Engineer.

Revise these test cases.

Current Test Cases:

{state["test_cases"]}

Reviewer Feedback:

{state["test_feedback"]}

Rules:

- Apply only the requested changes.
- Keep unchanged test cases.
- Do not add unnecessary tests.
- Return only the revised test cases.
"""

    revised_test_cases = invoke_llm(prompt)

    return {
        "test_cases": revised_test_cases
    }