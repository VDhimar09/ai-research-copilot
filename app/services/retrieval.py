from pathlib import Path

DOCUMENTS_DIR = Path("documents")

STOP_WORDS = {
    "the",
    "and",
    "for",
    "about",
    "what",
    "with",
    "from",
    "this",
    "that",
}


async def retrieve_documents(query: str):
    results = []

    query_clean = query.lower().strip()

    query_words = {
        word.strip(".,?!")
        for word in query_clean.split()
        if len(word.strip(".,?!")) > 2
        and word.strip(".,?!") not in STOP_WORDS
    }

    for file_path in DOCUMENTS_DIR.glob("*.txt"):
        content = file_path.read_text()
        content_lower = content.lower()

        matching_words = [
            word
            for word in query_words
            if word in content_lower
        ]

        score = len(matching_words)

        # Give an extra point when the complete search phrase appears.
        if query_clean in content_lower:
            score += 2

        if score > 0:
            results.append({
                "source": file_path.name,
                "content": content,
                "score": score,
                "matched_words": matching_words,
            })

    # Sort results by score in descending order
    results.sort(
        key=lambda result: result["score"],
        reverse=True,
    )

    if not results:
        return []

    top_score = results[0]["score"]

    return [
        result
        for result in results
        if result["score"] == top_score
    ]