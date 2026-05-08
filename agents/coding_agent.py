from graph.state import AgentState

from tools.ai_tools import ask_llm


def coding_agent(state: AgentState):

    user_input = state["user_input"]

    prompt = f"""
    You are an expert AI coding assistant.

    User Request:
    {user_input}

    Provide clean and professional code.
    """

    response = ask_llm(prompt)

    return {
        "response": response
    }