import asyncio

from app.services.retrieval import retrieve_documents


def test_retrieve_documents():
    results = asyncio.run(
        retrieve_documents("Company A")
    )

    assert results
    assert results[0]["source"]
    assert results[0]["content"]
    assert results[0]["score"] > 0