from graph.state import AgentState

from tools.memory_tools import (
    get_context,
    add_to_memory
)

from tools.ai_tools import ask_llm


def memory_agent(state: AgentState):

    try:

        user_input = state["user_input"]

        memory = state.get("conversation_history", [])

        context = get_context(memory)

        prompt = f"""
{context}

User: {user_input}

Provide a brief, direct response in 1-2 sentences.
"""

        response = ask_llm(prompt)

        memory = add_to_memory(
            "user",
            user_input,
            memory
        )

        memory = add_to_memory(
            "assistant",
            response,
            memory
        )

        return {
            "response": response,
            "conversation_history": memory
        }

    except Exception as e:

        return {
            "response": f"Error: {str(e)}",
            "conversation_history": state.get("conversation_history", [])
        }
