from app.services.llm import invoke_llm
from app.state.state import SDLCState


def generate_test_cases_node(state: SDLCState):

    prompt = f"""
You are a QA Engineer.

Generate concise test cases for this project skeleton.

Project:

{state["generated_code"]}

Generate ONLY:

- Functional Test Cases
- API Test Cases

Rules:
- Maximum 4 test cases.
- One line per test case.
- Do not explain.
"""

    test_cases = invoke_llm(prompt)

    print("\n======= GENERATED TEST CASES =======\n")
    print(test_cases)

    return {
        "test_cases": test_cases
    }