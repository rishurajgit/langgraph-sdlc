from app.state.state import SDLCState
from app.services.llm import invoke_llm

def design_node(state: SDLCState):
    
    design = f"""
    You are a Senior Software Architect.
    Base on the following user stories, generate a Software Design Document.
    
    Include:
    System Overview,
    Functional Requirements,
    Non-functional Requirements,
    High-level Architecture,
    Suggested Tech Stack,
    Database Design,
    API endpoints,
    Modules
    
    User Stories:
    {state["user_stories"]}
    
    Return only the Design Document.
    """
    
    design = invoke_llm(design)
    # print(design)
    return{
        "design_doc": design
    }