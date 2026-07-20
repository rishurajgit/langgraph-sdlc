# from google import genai

# from app.config.config import settings

# client = genai.Client(
#     api_key=settings.GEMINI_API_KEY
# )

# GEMINI_MODEL=settings.GEMINI_MODEL

# def invoke_llm(story: str) -> str:
#     response = client.models.generate_content(
#         model = GEMINI_MODEL,
#         contents=story
#     )
    
#     return response.text




#===============================================================================================================================================
# from langchain_groq import ChatGroq

# from app.config.config import settings


#   llm = ChatGroq(
#     api_key=settings.GROQ_API_KEY,
#     model=settings.GROQ_MODEL,
#     temperature=0.2,
# )


# def invoke_llm(prompt: str) -> str:
#     """
#     Sends the prompt to the Groq LLM and returns the response text.
#     """
#     response = llm.invoke(prompt)
#     return response.content

#==============================================================================================================#


from openai import OpenAI

from app.config.config import settings

client = OpenAI(
    api_key=settings.OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)


def invoke_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model=settings.OPENROUTER_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content