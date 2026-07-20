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
    
        "design_doc": "",
        "design_review_status": "",
        "design_feedback": "",
        
        "generated_code": "",
        "code_review_status": "",
        "code_review_attempts": 0,
        "code_feedback": "",
        
        "test_cases": "",
        "test_review_status": "",
        "test_feedback": "",
        "test_review_attempts": 0,
        
        "security_review_attempts": 0,
        
        "qa_status": "",
        "qa_report": "",
        "qa_attempts": 0,
        
        
        "deployment_status": "",
        "deployment_message": ""
        
        }
    )
    
    # print("\n=======FINAL STATE======")
    # print(result)
    return result
        # "status": "Workflow Started",
        # "message": "LangGraph workflow here"