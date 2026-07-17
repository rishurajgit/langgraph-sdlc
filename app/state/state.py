from typing import TypedDict

class SDLCState(TypedDict):
    # """
    # Shared state across the entire SDLC workflow.
    # """
    
    requirements: str
    user_stories: str
    review_status: str
    feedback: str
    
    design_doc: str
    design_review_status: str
    design_feedback: str
    
    generated_code: str
    code_review_status: str
    
    code_feedback: str
    
    security_review_status: str
    security_feedback: str
    secured_code: str