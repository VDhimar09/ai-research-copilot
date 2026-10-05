import asyncio

from app.services.retrieval import retrieve_documents


async def main():
    results = await retrieve_documents("Company A")

    for result in results:
        print(result)


asyncio.run(main())