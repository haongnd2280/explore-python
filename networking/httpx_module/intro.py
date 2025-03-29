import asyncio 

from httpx import AsyncClient


async def fetch_data():
    async with AsyncClient() as client:
        response = await client.get("http://example.com")
        print(response.text)


asyncio.run(fetch_data())
