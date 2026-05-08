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
You are Jarvis's supervisor.

Context:
{context}

User request: {user_input}

Available agents:
- system_agent (open apps, screenshot, shutdown, restart)
- browser_agent (search google, open youtube)
- coding_agent (code, programming)
- file_agent (read, write, list files)
- memory_agent (chat, follow-up)

If multiple tasks, return ALL agents needed in order, separated by commas.
If single task, return ONLY one agent name.

EXAMPLES:
"open chrome" -> system_agent
"open chrome and search for X" -> system_agent,browser_agent
"write code then save to file" -> coding_agent,file_agent

OUTPUT ONLY AGENT NAMES, NO OTHER TEXT.
"""

    response = ask_llm(prompt).strip().lower()

    # Parse agents from response
    agents = []

    for word in response.replace(",", " ").split():

        word = word.strip()

        if word in [
            "system_agent",
            "browser_agent",
            "coding_agent",
            "memory_agent",
            "file_agent"
        ] and word not in agents:

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
