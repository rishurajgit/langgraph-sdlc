from app.state.state import SDLCState

def deployment_node(state: SDLCState):
    
    print("\n===========DEPLOYMENT=============\n")
    
    prompt = """
    Deployment Recommendation
    The generated project is ready for deployment.
    
    Suggested Platforms:
    - Vercel
    - Render
    - Railway
    - AWS
    - Azure
    """
    
    print(prompt)
    
    return {
        "deployment_status": "Completed",
        "deployment_message": prompt.strip()
    }
    
    