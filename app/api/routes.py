from fastapi import APIRouter
from app.graph.workflow import graph
from app.api.schemas import WorkflowRequest



router = APIRouter()

@router.post("/run")
def run_workflow(request: WorkflowRequest):
    
    result = graph.invoke(
        {
        "requirements": request.requirements,
        "user_stories": "",
        "review_status": "",
        "feedback": "",
        "design_doc": ""
        }
    )
    
    # print("\n=======FINAL STATE======")
    # print(result)
    return result
        # "status": "Workflow Started",
        # "message": "LangGraph workflow here"