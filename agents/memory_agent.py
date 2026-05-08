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
You are Jarvis's memory system.

Context:
{context}

User: {user_input}

Based on the conversation history, provide a contextual response.
If this is a follow-up question, reference previous conversation.
Keep response concise and helpful.
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
            "response": f"Error in memory agent: {str(e)}",
            "conversation_history": state.get("conversation_history", [])
        }
