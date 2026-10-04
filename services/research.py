from services.retrieval import retrieve_documents


async def generate_research_answer(question: str):
    sources = await retrieve_documents(question)

    return {
        "question": question,
        "sources": sources
    }