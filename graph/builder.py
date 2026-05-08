from langgraph.graph import StateGraph
from langgraph.graph import END

from graph.state import AgentState

from tools.ai_tools import ask_llm

from tools.system_tools import (
    open_chrome,
    open_vscode,
    open_youtube,
    open_whatsapp,
    search_google,
    search_youtube,
    shutdown_pc,
    restart_pc,
    take_screenshot
)

from tools.file_tools import (
    list_directory,
    read_file,
    write_file,
    create_directory,
    delete_path,
    search_files
)


TOOLS = {
    "open_chrome": open_chrome,
    "open_vscode": open_vscode,
    "open_youtube": open_youtube,
    "open_whatsapp": open_whatsapp,
    "search_google": search_google,
    "search_youtube": search_youtube,
    "shutdown_pc": shutdown_pc,
    "restart_pc": restart_pc,
    "take_screenshot": take_screenshot,
    "list_directory": list_directory,
    "read_file": read_file,
    "write_file": write_file,
    "create_directory": create_directory,
    "delete_path": delete_path,
    "search_files": search_files
}


def jarvis_agent(state: AgentState):

    user_input = state["user_input"]

    memory = state.get("conversation_history", [])

    context = ""

    if memory:

        recent = memory[-5:]

        context = "\n".join(
            [f"{m['role']}: {m['content']}"
             for m in recent]
        )

    tool_descriptions = "\n".join(
        [f"- {name}: {func.__doc__ or 'No description'}"
         for name, func in TOOLS.items()]
    )

    prompt = f"""
You are Jarvis, an AI assistant.

Context:
{context}

User: {user_input}

Available tools:
{tool_descriptions}

INSTRUCTIONS:
1. Understand the user's request
2. Call the appropriate tool(s)
3. For compound requests, call multiple tools in order
4. Return the result

If opening YouTube and searching: call open_youtube, then search_youtube.
If asking to code: provide code directly.
"""

    # Get LLM response
    response = ask_llm(prompt)

    # Simple tool execution (for demo)
    response_text = str(response)

    # Execute tools based on keywords (temporary)
    if "open chrome" in user_input.lower():
        response_text = open_chrome()

    elif "open youtube" in user_input.lower():

        response_text = open_youtube()

        if "play" in user_input.lower() or "search" in user_input.lower():

            query = user_input

            for word in ["play", "search"]:
                if word in query:
                    parts = query.split(word)
                    if len(parts) > 1:
                        query = parts[1].strip()
                        break

            query = query.replace("youtube", "").replace("for", "").strip()

            if query:
                response_text += "\n" + search_youtube(query)

    elif "search" in user_input.lower():

        query = user_input.replace("search", "").replace("for", "").strip()

        response_text = search_google(query)

    else:

        response_text = response

    # Update memory
    memory.append({
        "role": "user",
        "content": user_input,
        "timestamp": ""
    })

    memory.append({
        "role": "assistant",
        "content": str(response_text),
        "timestamp": ""
    })

    return {
        "response": str(response_text),
        "conversation_history": memory
    }


# ====================================
# BUILD GRAPH
# ====================================

workflow = StateGraph(AgentState)

workflow.add_node(
    "jarvis_agent",
    jarvis_agent
)

workflow.set_entry_point(
    "jarvis_agent"
)

workflow.add_edge(
    "jarvis_agent",
    END
)

jarvis_graph = workflow.compile()
