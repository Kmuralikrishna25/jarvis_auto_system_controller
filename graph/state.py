from typing import TypedDict


class AgentState(TypedDict):

    user_input: str

    next_agent: str

    response: str