from app.services.evidence import build_evidence


def test_build_evidence():
    documents = [
        {
            "source": "company_a.txt",
            "content": "Company A announced a new manufacturing facility.",
            "score": 3,
        }
    ]

    evidence = build_evidence(documents)

    assert len(evidence) == 1
    assert evidence[0].source == "company_a.txt"
    assert evidence[0].content == "Company A announced a new manufacturing facility."
    assert evidence[0].score == 3