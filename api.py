from fastapi import FastAPI
from pydantic import BaseModel

import agent

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(query: Query):
    # return {"message": query.question}
    return agent.chat(query.question)
