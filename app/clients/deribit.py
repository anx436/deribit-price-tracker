import aiohttp
from app.core.config import settings

class DeribitClient:
    """Deribit client using aiohttp (as required)."""
    def __init__(self):
        self.base_url = settings.DERIBIT_BASE_URL

    async def get_index_price(self, index_name: str) -> float:
        """index_name must be lowercase: btc_usd or eth_usd"""
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.base_url}/public/get_index_price",
                params={"index_name": index_name.lower()}
            ) as response:
                response.raise_for_status()
                data = await response.json()
                return data["result"]["index_price"]
