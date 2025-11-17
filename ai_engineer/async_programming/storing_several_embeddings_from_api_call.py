import asyncio
import httpx

async def embed_text(client, text):
    r = await client.post(
        "https://api.openai.com/v1/embeddings",
        json={"input": text, "model": "text-embedding-3-large"},
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    return r.json()

async def main():
    texts = ["doc1...", "doc2...", "doc3..."]
    async with httpx.AsyncClient() as client:
        tasks = [embed_text(client, t) for t in texts]
        results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())
