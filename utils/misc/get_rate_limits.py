import aiohttp

from data import config


async def request_rate_limits():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://public-api.blablacar.com/api/v3/trips?key={config.BLABLACAR_API_TOKEN}") as response:
            result = response.headers.items()
            return result
