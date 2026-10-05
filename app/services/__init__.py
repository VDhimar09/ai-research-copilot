from app.agents.planner import create_research_plan


question = "What happened to Company A and what is happening in the manufacturing market?"

plan = create_research_plan(question)

print(plan)