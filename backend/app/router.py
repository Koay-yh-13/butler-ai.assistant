from fastapi import APIRouter, HTTPException

from app.ai.client import openrouter
from app.ai.prompts import SYSTEM_PROMPT
from app.models import ChatRequest

router = APIRouter()


@router.post("/chat")
async def chat(request: ChatRequest):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": request.message,
        },
    ]

    try:
        response = await openrouter.chat(messages)

        assistant = response["choices"][0]["message"]["content"]

        return {
            "response": assistant
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )
