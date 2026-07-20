from fastapi import FastAPI
from app.api.routes import router


app = FastAPI(
    title="LangGraph SDLC",
    description="SDLC Automation using LangGraph by AI"
)


app.include_router(router)