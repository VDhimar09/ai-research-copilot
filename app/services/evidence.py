def build_evidence(documents: list[dict]) -> list[dict]:
    evidence = []

    for document in documents:
        evidence.append({
            "source": document["source"],
            "content": document["content"],
            "score": document["score"],
        })

    return evidence