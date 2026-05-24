from typing import Annotated, NotRequired, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class RecoveryCase(TypedDict, total=False):
    case_id: NotRequired[str]
    summary: NotRequired[str]
    asset_type: NotRequired[str]
    asset_identifier: NotRequired[str]
    last_known_status: NotRequired[str]
    owner_context: NotRequired[str]


class RecoveryPilotState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    case: RecoveryCase
    risk_flags: list[str]
    next_actions: list[str]
