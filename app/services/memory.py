from mem0 import MemoryClient

from app.config.config import settings

memory = MemoryClient(
    api_key= settings.MEM0_API_KEY
)

USER_ID = "demo-user"


def save_memory(content: str, role: str = "user"):
    """Save information to Mem0."""
    memory.add(
        messages=[
            {
                "role": role,
                "content": content
            }
        ],
        user_id=USER_ID
    )


def get_memory_context(query: str) -> str:
    """Retrieve relevant memories as a formatted string."""

    response = memory.search(
        query=query,
        filters={
            "user_id": USER_ID
        }
    )

    memories = response.get("results", [])

    if not memories:
        return ""

    context = ""

    for item in memories:
        context += f"- {item['memory']}\n"

    return context.strip()