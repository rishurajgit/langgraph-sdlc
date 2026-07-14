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
        "feedback": ""
        }
    )
    return result
        # "status": "Workflow Started",
        # "message": "LangGraph workflow here"