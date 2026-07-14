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
    
