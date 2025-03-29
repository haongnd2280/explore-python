# Hàm này sẽ chạy 2 loại request đồng thời, một là OpenAI API requests và hai là HTTP requests.

import asyncio 

from httpx import AsyncClient 
from openai import AsyncOpenAI 


api_key = ""
client = AsyncOpenAI(api_key=api_key)

async def send_openai_request(prompt: str, **kwargs) -> str:
    """Send an asynchronous request to async OpenAI API.
    """

    response = await client.chat.completions.create(    # await AsyncOpenAI client
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        **kwargs
    )

    content = response.choices[0].message.content    # extract the respons
    return content

async def send_httpx_request(url: str) -> str:
    """Send an asynchronous HTTP request to a given URL using httpx.
    """

    async with AsyncClient() as client:
        response = await client.get(url)
        return response.text[:100]      # return the first 100 characters
    

async def main():
    """Hàm này sẽ chạy 2 phần, một là OpenAI requests và hai là HTTP requests.
    """

    # Define multiple prompts for OpenAI API 
    prompts = [
        "Explain quantum entanglement in simple terms.",
        "What are some use cases of HTTP/2?",
        "Summarize the book '1984' by George Orwell.",
    ]

    # Define multiple URLs to fetch concurrently
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
    ]

    # Create tasks for OpenAI API requests
    openai_tasks = [send_openai_request(prompt) for prompt in prompts]

    # Create tasks for HTTP requests
    httpx_tasks = [send_httpx_request(url) for url in urls]

    # Run all tasks concurrently
    responses = await asyncio.gather(*openai_tasks, *httpx_tasks)

    return responses 


if __name__ == "__main__":
    import time 

    start = time.time()
    responses = asyncio.run(main())
    end = time.time()

    for response in responses:
        print(response)
    
    print(f"Time taken: {end - start:.2f} seconds")
