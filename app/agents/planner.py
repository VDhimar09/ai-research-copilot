def create_research_plan(question: str) -> list[dict]:
    question_lower = question.lower()

    tasks = []

    if "company a" in question_lower:
        tasks.append({
            "type": "search",
            "query": "Company A"
        })

    if "company b" in question_lower:
        tasks.append({
            "type": "search",
            "query": "Company B"
        })

    if "market" in question_lower or "manufacturing" in question_lower:
        tasks.append({
            "type": "search",
            "query": "European manufacturing"
        })

    if not tasks:
        tasks.append({
            "type": "search",
            "query": question
        })

    return tasks