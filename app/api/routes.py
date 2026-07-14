from fastapi import APIRouter
from app.graph.workflow import graph

router = APIRouter()

@router.post("/run")
def run_workflow():
    
    result = graph.invoke(
        {
        "requirements": "Build an AI SDLC Automation Platform",
        "user_stories": "",
        "review_status": "",
        "feedback": "",
        "design_doc": ""
        }
    )
    
    print("\n=======FINAL STATE======")
    print(result)
    return result
        # "status": "Workflow Started",
        # "message": "LangGraph workflow here"