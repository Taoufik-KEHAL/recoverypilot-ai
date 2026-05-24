from fastapi import FastAPI
from pydantic import BaseModel, Field
from recoverypilot_assistant import RecoveryCase, run_recoverypilot_turn

from recoverypilot_api.config import settings


class HealthResponse(BaseModel):
    status: str = "ok"
    service: str = "recoverypilot-api"
    environment: str


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1)
    case: RecoveryCase | None = None


class ChatResponse(BaseModel):
    reply: str
    case: RecoveryCase
    risk_flags: list[str]
    next_actions: list[str]


app = FastAPI(
    title="RecoveryPilot AI API",
    version="0.1.0",
    description="API for the RecoveryPilot AI asset recovery assistant.",
)


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(environment=settings.environment)


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    state = run_recoverypilot_turn(message=request.message, case=request.case)
    reply = str(state["messages"][-1].content)

    return ChatResponse(
        reply=reply,
        case=state["case"],
        risk_flags=state["risk_flags"],
        next_actions=state["next_actions"],
    )
