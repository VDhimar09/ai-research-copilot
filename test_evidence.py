from app.services.evidence import build_evidence


documents = [
    {
        "source": "company_a.txt",
        "content": "Company A announced a new manufacturing facility.",
        "score": 3,
    }
]

evidence = build_evidence(documents)

print(evidence)