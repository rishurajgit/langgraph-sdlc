from google import genai

from app.config.config import settings

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)

GEMINI_MODEL=settings.GEMINI_MODEL

def invoke_llm(story: str) -> str:
    response = client.models.generate_content(
        model = GEMINI_MODEL,
        contents=story
    )
    
    return response.text