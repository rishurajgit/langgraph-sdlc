# from app.state.state import SDLCState

# def code_review_node(state: SDLCState):
    
#     print("\n======= CODE REVIEW ==========\n")
    
#     preview = state["generated_code"]
#     print(preview)
    
#     if len(state["generated_code"]) > 1200:
#         print("\n... Code truncated ...\n")

#     decision = input(
#         "\nApprove Code? (approved / feedback): "
#     ).strip().lower()

#     if decision == "approved":
#         return {
#             "code_review_status": "approved",
#             "code_feedback": ""
#         }

#     feedback = input("Enter Code Feedback: ")

#     return {
#         "code_review_status": "feedback",
#         "code_feedback": feedback
#     }


from app.state.state import SDLCState
from app.services.llm import invoke_llm

def code_review_node(state: SDLCState):
    attempts = state["code_review_attempts"] + 1
    
    
    prompt = f"""
You are a Senior Software Architect.

Review this project skeleton.

Project Skeleton:

{state["generated_code"]}

Evaluate ONLY:

- Folder structure
- Module organization
- Naming
- Separation of concerns
- Architecture

Ignore:
- Missing business logic
- Missing CRUD
- Missing authentication implementation
- Missing database implementation
- Missing tests

Decision Rules:

- If architecture is acceptable, return:

STATUS: approved

Feedback:
None

- Return STATUS: feedback ONLY if there are major architectural issues.

Reply ONLY in one of these formats:

STATUS: approved

Feedback:
None

OR

STATUS: feedback

Feedback:
<max 30 words>
"""
        
    review = invoke_llm(prompt)
    
    print("\n======= CODE REVIEW ======\n")
    print(review)
    
    if "STATUS: APPROVED" in review.upper():
        return {
            "code_review_status": "approved",
            "code_feedback": "",
            "code_review_attempts": attempts
        }

    # feedback = review.split("Feedback:")[-1].strip()
    
    feedback = ""

    if "FEEDBACK:" in review.upper():
        feedback = review.split("Feedback:", 1)[-1].strip()

    return {
        "code_review_status": "feedback",
        "code_feedback": feedback,
        "code_review_attempts": attempts
    }