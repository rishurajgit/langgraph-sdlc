from app.state.state import SDLCState
from app.services.llm import invoke_llm

def code_generation_node(state: SDLCState):
    prompt = f"""
    You are a senior Python backend developer.
    Based on the following Software Design Document, generate clean and production ready backend code
    Design Document:
    {state['design_doc']}
    
    Requirements:
    - Use the required language to generate code
    - Use FastAPI for endpoints
    - Follow clean coding practice
    - Add meaningfull comments
    - Organize the code logically
    
    Rules:
    - Generate only the Source Code.
    - Do not use Markdown.
    - No need to explain the code.
    - Keep the response concise.
    """
    generated_code = invoke_llm(prompt)
    
    return{
        "generated_code": generated_code
    }