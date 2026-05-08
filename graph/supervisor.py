from graph.state import AgentState

from tools.ai_tools import ask_llm


def supervisor(state: AgentState):

    user_input = state["user_input"]

    memory = state.get("conversation_history", [])

    context = ""

    if memory:

        recent = memory[-5:]

        context = "\n".join(
            [f"{m['role']}: {m['content']}"
             for m in recent]
        )

    prompt = f"""
You are Jarvis's router.

User: {user_input}

RULES:
- "open youtube" or "play X" -> browser_agent
- "search google" or "search for X" -> browser_agent
- "open chrome/vscode" -> system_agent
- Multiple tasks -> return all agents, comma separated

EXAMPLES:
Q: open youtube
A: browser_agent

Q: open chrome and search for X
A: system_agent,browser_agent

Q: play python tutorial on youtube
A: browser_agent

OUTPUT ONLY AGENT NAMES:
"""

    response = ask_llm(prompt).strip().lower()

    # Aggressive parsing - extract only valid agent names
    agents = []

    valid = [
        "system_agent",
        "browser_agent",
        "coding_agent",
        "memory_agent",
        "file_agent"
    ]

    # Check if response contains agent names
    for agent in valid:

        if agent in response and agent not in agents:

            agents.append(agent)

    # If no agents found, use LLM response as-is if valid
    if not agents:

        for word in response.split():

            word = word.strip(".,;:")

            if word in valid and word not in agents:

                agents.append(word)

    if agents:

        return {
            "next_agent": agents[0],
            "pending_agents": agents[1:]
        }

    return {
        "next_agent": "memory_agent",
        "pending_agents": []
    }

    return {
        "next_agent": "memory_agent",
        "pending_agents": []
    }
