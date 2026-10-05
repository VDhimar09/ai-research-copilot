from app.agents.planner import create_research_plan
from app.services.evidence import build_evidence
from app.services.retrieval import retrieve_documents
from app.services.analysis import generate_final_answer


async def generate_research_answer(question: str):
    plan = create_research_plan(question)

    results = []

    for task in plan:
        documents = await retrieve_documents(task["query"])
        evidence = build_evidence(documents)

        results.append({
            "task": task,
            "evidence": evidence,
        })

    answer = generate_final_answer(results)

    return {
        "question": question,
        "answer": answer,
        "plan": plan,
        "results": results,
    }