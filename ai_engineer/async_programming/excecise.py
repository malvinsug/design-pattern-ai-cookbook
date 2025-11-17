"""
🧪 Exercise: Fix the Async Code for Parallel LLM Calls

You are building a small evaluation script that sends 3 prompts to a model in parallel.
The code below tries to use async, but it is broken because the developer doesn’t know where to place async and await.

Your job is to rewrite it so the 3 calls run concurrently.
"""


import httpx

def call_model(prompt):
    client = httpx.AsyncClient()
    response = client.post(
        "https://example.com/llm",
        json={"prompt": prompt}
    )
    return response.json()

def main():
    prompts = ["test1", "test2", "test3"]
    results = []
    for p in prompts:
        result = call_model(p)
        results.append(result)
    print(results)

main()

"""
import asyncio
import httpx

# 1. Any function that performs awaitable operations must be async
async def call_model(prompt):
    # 2. AsyncClient must be used with "async with"
    async with httpx.AsyncClient() as client:
        # 3. POST request must be awaited
        response = await client.post(
            "https://example.com/llm",
            json={"prompt": prompt}
        )
        return response.json()

# 4. Main must also be async since it will await things
async def main():
    prompts = ["test1", "test2", "test3"]

    # 5. Launch all calls concurrently
    tasks = [call_model(p) for p in prompts]

    # 6. Use await on asyncio.gather to get all results
    results = await asyncio.gather(*tasks)

    print(results)

# 7. Run the async event loop
asyncio.run(main())

"""