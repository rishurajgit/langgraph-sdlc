from app.state.state import SDLCState
from app.services.memory import  save_memory

def user_requirements_node(state: SDLCState):
    """
    First node of the workflow.
    """
    
    print("Recieved Requirements:")
    print(state["requirements"])
    
    save_memory(state["requirements"])
    
    return{
        "requirements": state["requirements"]
    }
