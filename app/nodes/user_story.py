from app.state.state import SDLCState
from app.services.llm import invoke_llm
from app.services.memory import get_memory_context


def generate_user_story_node(state: SDLCState):
    
    requirement = state["requirements"]
    memory_context = get_memory_context(requirement)
    print("\n========== MEMORY CONTEXT ==========")
    print(memory_context)
    print("====================================\n")
    
    story = f"""
You are an experienced Product Owner.

Previous Project Memory:
{memory_context}

Current Requirement:
{requirement}

Generate the most relevant Agile user stories.

Format:

Story 1
As a <role>,
I want <feature>,
So that <benefit>.

Rules:
- Generate ONLY the 2 most important user stories.
- Prioritize the current requirement.
- Use previous memory only if it is relevant.
- Return only the user stories.
"""
    
    stories = invoke_llm(story)
    return {
        "user_stories": stories
    }