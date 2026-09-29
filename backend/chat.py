from fastapi import APIRouter

router = APIRouter()

@router.get("/chat")
def chat():
    return {
        "message": "MyMemory AI is ready!",
        "memory": "Hindsight long-term memory will be connected here."
    }
