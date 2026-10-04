import asyncio

from services.retrieval import retrieve_documents


async def main():
    results = await retrieve_documents("Company Z")

    for result in results:
        print(result)


asyncio.run(main())