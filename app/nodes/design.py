from app.state.state import SDLCState
from app.services.llm import invoke_llm
from app.services.memory import get_memory_context


def design_node(state: SDLCState):
    
    memory_context = get_memory_context(
        state["requirements"]
    )
    
    design = f"""
    You are a Senior Software Architect.
    
    Previous Project Memory:
    {memory_context}
    
    User Stories:
    {state["user_stories"]}
    
    generate a  concise Software Design Document.
    
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