from app.state.state import SDLCState

def generate_user_story_node(state: SDLCState):
    
    requirement = state["requirements"]
    
    story = f"""
    As a user,
    i want {requirement}
    so that i can achieve my goal.
    """
    
    return {
        "user_stories": story
    }