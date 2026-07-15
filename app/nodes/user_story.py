from app.state.state import SDLCState
from app.services.llm import invoke_llm

def generate_user_story_node(state: SDLCState):
    
    requirement = state["requirements"]
    
    story = f"""
    You are an experienced Product Owner.
    Generate professional Agile user stories.
    Requirement:
    {requirement}
    Return only the user stories.
    """
    
    stories = invoke_llm(story)
    return {
        "user_stories": stories
    }