from pathlib import Path


DOCUMENTS_DIR = Path("documents")


async def retrieve_documents(query: str):
    results = []

    for file_path in DOCUMENTS_DIR.glob("*.txt"):
        content = file_path.read_text()

        if query.lower() in content.lower():
            results.append({
                "source": file_path.name,
                "content": content
            })

    return results