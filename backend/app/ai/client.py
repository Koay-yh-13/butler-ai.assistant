import httpx

from app.config import CONFIG


class OpenRouterClient:
    BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

    async def chat(self, messages):
        if not CONFIG.openrouter_api_key:
            raise ValueError(
                "OpenRouter API key has not been configured."
            )

        headers = {
            "Authorization": f"Bearer {CONFIG.openrouter_api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": CONFIG.model,
            "messages": messages,
        }

        async with httpx.AsyncClient(timeout=120) as client:
            response = await client.post(
                self.BASE_URL,
                headers=headers,
                json=payload,
            )

        response.raise_for_status()

        return response.json()


openrouter = OpenRouterClient()
