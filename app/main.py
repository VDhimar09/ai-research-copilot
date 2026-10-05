from fastapi import FastAPI
from pydantic import BaseModel

from app.services.research import generate_research_answer

app = FastAPI()


class ResearchRequest(BaseModel):
    question: str

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/research")
async def research(request: ResearchRequest):
    return await generate_research_answer(request.question) 