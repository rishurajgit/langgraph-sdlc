from pydantic import BaseModel

class WorkflowRequest(BaseModel):
    requirements: str
    
class WorkflowResponses(BaseModel):
    requirements: str
    user_stories: str
    review_status: str
    feedback: str
    
    design_doc: str
    design_review_status: str
    design_feedback: str
    
    generated_code: str
    code_review_status: str
    code_feedback: str