from app.agents.planner import create_research_plan


def test_create_research_plan():
    question = "What happened to Company A and what is happening in the manufacturing market?"

    plan = create_research_plan(question)

    assert len(plan) == 2
    assert plan[0]["query"] == "Company A"
    assert plan[1]["query"] == "European manufacturing"