results = await asyncio.gather(
    search_pinecone(query),
    search_weaviate(query),
    fetch_arxiv(query)
)