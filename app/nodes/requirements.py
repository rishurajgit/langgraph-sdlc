from app.state.state import SDLCState

def user_requirements_node(state: SDLCState):
    """
    First node of the workflow.
    """
    
    print("Recieved Requirements:")
    print(state["requirements"])
    
    return{}
    