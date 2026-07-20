from app.services.llm import invoke_llm
from app.state.state import SDLCState

def revise_design_node(state: SDLCState):
    prompt = f"""
    You are a Senior Software Architect.

Revise the following Software Design Document.

Current Design:

{state["design_doc"]}

Reviewer Feedback:

{state["design_feedback"]}

Update the design according to the feedback.

Return only the revised Design Document.
"""

    revised_design = invoke_llm(prompt)
    
    return{
        "design_doc": revised_design
    }