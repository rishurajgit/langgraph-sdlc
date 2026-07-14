from fastapi import APIRouter

router = APIRouter()

@router.post("/run")
def run_workflow():
    return{
        "status": "Workflow Started",
        "message": "LangGraph workflow here"
    }