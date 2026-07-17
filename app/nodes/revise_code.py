from app.services.llm import invoke_llm
from app.state.state import SDLCState


def revise_code_node(state: SDLCState):

    prompt = f"""
You are a Senior Software Engineer.

Revise the generated code using the review feedback.

Generated Code:

{state["generated_code"]}

Reviewer Feedback:

{state["code_feedback"]}

Rules:
- Apply only the requested changes.
- Preserve the existing functionality.
- Return ONLY the updated source code.
"""

    updated_code = invoke_llm(prompt)

    return {
        "generated_code": updated_code
    }