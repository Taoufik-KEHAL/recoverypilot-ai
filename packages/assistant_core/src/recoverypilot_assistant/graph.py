from typing import cast

from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph

from recoverypilot_assistant.state import RecoveryCase, RecoveryPilotState


def _last_user_message(state: RecoveryPilotState) -> str:
    for message in reversed(state["messages"]):
        if isinstance(message, HumanMessage):
            return str(message.content)
    return ""


def intake_node(state: RecoveryPilotState) -> RecoveryPilotState:
    message = _last_user_message(state)
    normalized = message.lower()
    case = RecoveryCase(**state.get("case", {}))

    if not case.get("summary"):
        case["summary"] = message

    if not case.get("asset_type"):
        if any(term in normalized for term in ("crypto", "wallet", "seed phrase", "exchange")):
            case["asset_type"] = "digital_asset"
        elif any(term in normalized for term in ("server", "backup", "database", "system")):
            case["asset_type"] = "it_asset"
        elif any(term in normalized for term in ("insurance", "claim", "policy")):
            case["asset_type"] = "insurance_or_legal_asset"
        elif any(term in normalized for term in ("bank", "wire", "fund", "payment")):
            case["asset_type"] = "financial_asset"
        else:
            case["asset_type"] = "unspecified"

    risk_flags = list(state.get("risk_flags", []))
    if any(term in normalized for term in ("lawsuit", "police", "attorney", "court", "regulator")):
        risk_flags.append("possible_legal_sensitivity")
    if any(term in normalized for term in ("password", "private key", "seed phrase", "ssn")):
        risk_flags.append("sensitive_secret_or_personal_data")

    return {
        **state,
        "case": case,
        "risk_flags": sorted(set(risk_flags)),
    }


def planner_node(state: RecoveryPilotState) -> RecoveryPilotState:
    case = state["case"]
    next_actions = list(state.get("next_actions", []))

    if case.get("asset_type") == "unspecified":
        next_actions.append("Clarify the type of asset and the recovery objective.")

    next_actions.extend(
        [
            "Record the asset identifier, ownership evidence, and last known status.",
            "Build a dated timeline of events and communications.",
            "Separate verified facts from assumptions or missing information.",
        ]
    )

    if "sensitive_secret_or_personal_data" in state.get("risk_flags", []):
        next_actions.append(
            "Redact secrets and sensitive personal data before sharing case material."
        )

    return {
        **state,
        "next_actions": list(dict.fromkeys(next_actions)),
    }


def responder_node(state: RecoveryPilotState) -> RecoveryPilotState:
    case = state["case"]
    asset_type = case.get("asset_type", "unspecified")
    next_actions = state.get("next_actions", [])
    risk_flags = state.get("risk_flags", [])

    response_parts = [
        f"I started a recovery case profile and classified the asset type as `{asset_type}`.",
        (
            "The immediate goal is to preserve facts, avoid risky assumptions, "
            "and identify the next verifiable actions."
        ),
    ]

    if risk_flags:
        response_parts.append(f"Risk flags noted: {', '.join(risk_flags)}.")

    if next_actions:
        action_text = "\n".join(f"- {action}" for action in next_actions[:5])
        response_parts.append(f"Recommended next actions:\n{action_text}")

    response_parts.append(
        "I can help turn this into a structured case timeline, evidence checklist, "
        "or recovery plan."
    )

    return {
        **state,
        "messages": [AIMessage(content="\n\n".join(response_parts))],
    }


def create_recoverypilot_graph() -> CompiledStateGraph[
    RecoveryPilotState, None, RecoveryPilotState, RecoveryPilotState
]:
    graph = StateGraph(RecoveryPilotState)
    graph.add_node("intake", intake_node)
    graph.add_node("planner", planner_node)
    graph.add_node("responder", responder_node)

    graph.add_edge(START, "intake")
    graph.add_edge("intake", "planner")
    graph.add_edge("planner", "responder")
    graph.add_edge("responder", END)

    return graph.compile()


def run_recoverypilot_turn(
    message: str,
    case: RecoveryCase | None = None,
) -> RecoveryPilotState:
    graph = create_recoverypilot_graph()
    initial_state: RecoveryPilotState = {
        "messages": [HumanMessage(content=message)],
        "case": case or RecoveryCase(),
        "risk_flags": [],
        "next_actions": [],
    }
    return cast(RecoveryPilotState, graph.invoke(initial_state))
