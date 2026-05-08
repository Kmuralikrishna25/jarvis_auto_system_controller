from graph.state import AgentState

from tools.ai_tools import ask_llm


# Keywords for direct routing (bypass LLM)
SYSTEM_KEYWORDS = [
    "open chrome", "open vscode", "open youtube",
    "open whatsapp", "shutdown", "restart",
    "screenshot", "search google"
]

FILE_KEYWORDS = [
    "list", "show files", "read file", "open file",
    "create directory", "make folder", "search for", "find files"
]


def supervisor(state: AgentState):

    user_input = state["user_input"].lower()

    # ==========================================
    # DIRECT KEYWORD MATCHING (BYPASS LLM)
    # ==========================================

    # System commands
    if any(kw in user_input for kw in SYSTEM_KEYWORDS):
        return {"next_agent": "system_agent"}

    # File commands
    if any(kw in user_input for kw in FILE_KEYWORDS):
        return {"next_agent": "file_agent"}

    # ==========================================
    # LLM-BASED ROUTING FOR COMPLEX QUERIES
    # ==========================================

    memory = state.get("conversation_history", [])

    context = ""
    if memory:
        recent = memory[-5:]
        context = "Previous: " + " | ".join(
            [m["content"] for m in recent]
        )

    prompt = f"""
{context}

User: {user_input}

Route to: system_agent, browser_agent, coding_agent, file_agent, or memory_agent.
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
