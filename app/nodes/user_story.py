from app.state.state import SDLCState
from app.services.llm import invoke_llm

def generate_user_story_node(state: SDLCState):
    
    requirement = state["requirements"]
    
    # story = f"""
    # You are an experienced Product Owner.
    # Generate professional Agile user stories.
    # Requirement:
    # {requirement}
    # Return only the user stories.
    # """
    story = f"""
    You are an experienced Product Owner.

Generate ONLY the 5 most important Agile user stories.

Requirement:
{requirement}

Format:

Story 1
As a <role>,
I want <feature>,
So that <benefit>.

Rules:
- Maximum 2 user stories.
- Each story should be 2-3 lines.
- Prioritize core functionality.
- Return only the user stories.
"""
    
    stories = invoke_llm(story)
    return {
        "user_stories": stories
    }