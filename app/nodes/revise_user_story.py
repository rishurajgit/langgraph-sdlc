from app.state.state import SDLCState
from app.services.llm import invoke_llm


def revise_user_story_node(state: SDLCState):
    prompt = f"""
    You are an experienced Product Owner.

Revise the following Agile User Stories based on the review feedback also your task is to EDIT existing user stories

Current User Stories:

{state["user_stories"]}

Reviewer Feedback:

{state["feedback"]}

Rules:
- You must follow the feedback exactly
- Keep only the stories requested
- Remove stories only if requested.
- Do not create unnecessary new stories.
- Return ONLY the revised user stories.
"""
    # story = state["user_stories"]
    # feedback = state["feedback"]
    # revised_story = story + f"\n\nRevision:\n{feedback}"
    revised_story =invoke_llm(prompt)
    print("\n========== REVISED STORIES ==========\n")
    print(revised_story)
    print("\n=====================================\n")
    return{
        "user_stories": revised_story
    }