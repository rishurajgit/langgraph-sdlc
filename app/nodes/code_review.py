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
    
    # prompt = f"""
    # You are a Senior Engineer perfomring a code review.
    # Review the following generated source code.
    
    # Generated code:
    # {state["generated_code"]}
    
    # Evalute:
    # 1. Code Quality
    # 2. Readability
    # 3. Maintainability
    # 4. Naming Conventions
    # 5. Architecture
    # 6. Error Handling
    # 7. Best Practice
    
    # Rules:
    # - if the code is acceptable, respond exactly as:
    
    # STATUS: approved
    
    # - Otherwise respond exactly as:
    # STATUS: feedback
    
    # Feedback:
    # <your feedback>
    
    # Do not rewrite the code.
    # Keep the feedback concise.
    # """
    prompt = f"""
You are a Senior Software Engineer performing a code review.

Review the following generated project skeleton.

Generated Code:

{state["generated_code"]}

Evaluate ONLY:

1. Naming
2. Architecture
3. Separation of Concerns
4. Folder Organization

Decision Rules:

- If there are only MINOR improvements or style suggestions,
  return:

STATUS: approved

Feedback:
<optional suggestions>

- Return STATUS: feedback ONLY if there are MAJOR architectural,
  structural, or design problems that must be fixed before proceeding.

Keep feedback under 50 words.

Do not rewrite the code.
Reply ONLY in this format:

STATUS: approved

Feedback:
...

OR

STATUS: feedback

Feedback:
...
"""
        
    review = invoke_llm(prompt)
    
    print("\n======= CODE REVIEW ======\n")
    print(review)
    
    if "STATUS: APPROVED" in review.upper():
        return {
            "code_review_status": "approved",
            "code_feedback": ""
        }

    # feedback = review.split("Feedback:")[-1].strip()
    
    feedback = ""

    if "FEEDBACK:" in review.upper():
        feedback = review.split("Feedback:", 1)[-1].strip()

    return {
        "code_review_status": "feedback",
        "code_feedback": feedback
    }