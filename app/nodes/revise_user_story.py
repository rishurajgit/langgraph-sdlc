from app.state.state import SDLCState

def revise_user_story_node(state: SDLCState):
    
    story = state["user_stories"]
    feedback = state["feedback"]
    revised_story = story + f"\n\nRevision:\n{feedback}"
    
    return{
        "user_stories": revised_story
    }