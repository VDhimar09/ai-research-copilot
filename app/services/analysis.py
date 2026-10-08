from app.models.evidence import Evidence


def generate_final_answer(results: list[dict]) -> str:
    statements = []

    for result in results:
        evidence_items: list[Evidence] = result["evidence"]

        for evidence in evidence_items:
            content = evidence.content.strip()
            source = evidence.source

            statements.append(
                f"According to {source}: {content}"
            )

    if not statements:
        return "I could not find enough evidence to answer the question."

    return " ".join(statements)