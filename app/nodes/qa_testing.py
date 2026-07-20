from app.services.llm import invoke_llm
from app.state.state import SDLCState


def qa_testing_node(state: SDLCState):
    attempts = state["qa_attempts"] + 1

    prompt = f"""
You are a Senior QA Engineer.

Project Skeleton:

{state["generated_code"]}

Test Cases:

{state["test_cases"]}

Evaluate whether the project is ready for deployment.

Return ONLY in this format:

STATUS: PASS

Report:
<short report>

OR

STATUS: FAIL

Report:
<short report>

Keep the report under 80 words.
"""

    result = invoke_llm(prompt)

    print("\n======= QA TESTING =======\n")
    print(result)

    status = "FAIL"

    if "STATUS: PASS" in result.upper():
        status = "PASS"

    report = ""

    if "REPORT:" in result.upper():
        report = result.split("Report:", 1)[-1].strip()

    return {
        "qa_status": status,
        "qa_report": report,
        "qa_attempts": attempts
    }