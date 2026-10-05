def generate_final_answer(results: list[dict]) -> str:
    statements = []

    for result in results:
        for evidence in result["evidence"]:
            content = evidence["content"].strip()
            source = evidence["source"]

            statements.append(
                f"According to {source}: {content}"
            )

    if not statements:
        return "I could not find enough evidence to answer the question."

    return " ".join(statements)