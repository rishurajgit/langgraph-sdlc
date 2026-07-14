from pydantic import BaseModel

class WorkflowRequest(BaseModel):
    requirements: str
    
class WorkflowResponses(BaseModel):
    requirements: str
    user_stories: str
    review_status: str
    feedback: str
    design_doc: str