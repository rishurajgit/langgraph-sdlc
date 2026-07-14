from app.state.state import SDLCState

def design_node(state: SDLCState):
    
    design = f"""
    Design Document
    Based on User Stories
    {state["user_stories"]}
    """
    print(design)
    return{
        "design_doc": design
    }