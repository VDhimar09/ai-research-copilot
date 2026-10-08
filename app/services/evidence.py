from app.models.evidence import Evidence


def build_evidence(documents: list[dict]) -> list[Evidence]:
    return [
        Evidence(
            source=document["source"],
            content=document["content"],
            score=document["score"],
        )
        for document in documents
    ]