from typing import Optional

import httpx

from app.config import settings


async def get_user_by_id(user_id: str) -> Optional[dict]:
    url = f"{settings.USERS_API_BASE}/users/{user_id}"
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            response = await client.get(url)
            if response.status_code in (200, 201):
                return response.json()
            return None
        except httpx.RequestError:
            return None
