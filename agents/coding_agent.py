from graph.state import AgentState

from tools.ai_tools import ask_llm


def coding_agent(state: AgentState):

    try:

        user_input = state["user_input"]

        prompt = f"""
User: {user_input}

Provide clean code only. No explanations unless asked.
"""

        response = ask_llm(prompt)

        return {
            "response": response
        }

    except Exception as e:

        return {
            "response": f"Error: {str(e)}"
        }