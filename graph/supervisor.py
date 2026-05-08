from graph.state import AgentState

from tools.ai_tools import ask_llm


def supervisor(state: AgentState):

    user_input = state["user_input"]

    memory = state.get(
        "conversation_history",
        []
    )

    context = ""

    if memory:

        recent = memory[-5:]

        context = "Previous: " + " | ".join(
            [m["content"] for m in recent]
        )

    prompt = f"""
You are Jarvis's supervisor.

{context}

User request: {user_input}

Decide which agent should handle this:
- system_agent: OS commands, open apps, shutdown, restart, screenshot
- browser_agent: web search, YouTube, browsing
- coding_agent: code, programming, debugging
- memory_agent: follow-up questions, context-aware requests
- file_agent: file operations, read/write, list directories

Respond with ONLY the agent name.
"""

    response = ask_llm(prompt).strip().lower()

    valid_agents = [
        "system_agent",
        "browser_agent",
        "coding_agent",
        "memory_agent",
        "file_agent"
    ]

    if response in valid_agents:
        return {"next_agent": response}

    return {"next_agent": "memory_agent"}
