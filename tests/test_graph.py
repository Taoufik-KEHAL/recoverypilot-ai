from langchain_core.messages import AIMessage
from recoverypilot_assistant import run_recoverypilot_turn


def test_graph_classifies_digital_asset() -> None:
    state = run_recoverypilot_turn("I need help recovering a crypto wallet.")

    assert state["case"]["asset_type"] == "digital_asset"
    assert state["next_actions"]
    assert isinstance(state["messages"][-1], AIMessage)


def test_graph_flags_sensitive_secrets() -> None:
    state = run_recoverypilot_turn("I lost access and found an old seed phrase.")

    assert "sensitive_secret_or_personal_data" in state["risk_flags"]
    assert any("Redact secrets" in action for action in state["next_actions"])
