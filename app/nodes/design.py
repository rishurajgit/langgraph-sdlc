from app.state.state import SDLCState
from app.services.llm import invoke_llm

def design_node(state: SDLCState):
    
    design = f"""
    You are a Senior Software Architect.
    Base on the following user stories, generate a Software Design Document.
    
    Include:
    1. System Overview,
    - (1-2 sentences)
    
    2. Functional Requirements,
    - maximum 1-2 bullet points
    
    3. Non-functional Requirements,
    - Maximum 2 bullet points
    
    4. High-level Architecture,
    - Explain in  1-2 bullet points
    
    5. Suggested Tech Stack,
    - Backend
    - Database
    
    6. Database Design,
    - Mention only main entities
    - Maximum 3 entities
    
    7. API endpoints,
    - Only important endpoint
    - Format:
    Method / endpoint - Purpose
    
    8. Modules
    - Maximum 2 modules
    
    Rules:
    1. Keep the entire document under 500 words.
    2. Use Markdown headings.
    3. Use bullet points instead of long paragraphs.
    4. Do not include implementation details.
    5. Do not generate source code.
    6. Do not repeat information.
    7. Return ONLY the Design Document.
    
    User Stories:
    {state["user_stories"]}
    
    Return only the Design Document.
    """
    
    design = invoke_llm(design)
    # print(design)
    return{
        "design_doc": design
    }