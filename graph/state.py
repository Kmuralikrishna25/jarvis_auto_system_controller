from typing import TypedDict, List, Dict, Any


class AgentState(TypedDict):

    user_input: str

    next_agent: str

    response: str

    conversation_history: List[Dict[str, str]]

    context: Dict[str, Any]