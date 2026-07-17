from app.services.llm import invoke_llm
from app.state.state import SDLCState


def fix_security_node(state: SDLCState):

    skeleton = state["generated_code"][:2000]
    prompt = f"""
You are a Security Engineer.

Review this project skeleton.
{skeleton}

Skeleton:
{state["generated_code"]}

Feedback:
{state["security_feedback"]}

Rules:
- Fix only the reported issue.
- Keep existing structure.
- Return only the updated skeleton.
"""

    secured_code = invoke_llm(prompt)

    return {
        "generated_code": secured_code,
        "secured_code": secured_code
    }