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
    
