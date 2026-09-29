import os
from fastapi import FastAPI
from pydantic import BaseModel
from hindsight_client import Hindsight

app = FastAPI(title="MyMemory AI")

hindsight = Hindsight(
    base_url=os.getenv("HINDSIGHT_URL", "http://localhost:8888"),
    api_key=os.getenv("HINDSIGHT_API_KEY")
)

BANK_ID = "mymemory-user"


class Message(BaseModel):
    text: str


@app.get("/")
def home():
    return {
        "app": "MyMemory AI",
        "status": "running"
    }


@app.post("/remember")
def remember(message: Message):
    hindsight.retain(
        bank_id=BANK_ID,
        content=message.text,
        context="MyMemory AI conversation"
    )

    return {
        "success": True,
        "message": "Memory stored"
    }


@app.post("/recall")
def recall(message: Message):
    result = hindsight.recall(
        bank_id=BANK_ID,
        query=message.text
    )

    memories = [item.text for item in result.results]

    return {
        "query": message.text,
        "memories": memories
    }
