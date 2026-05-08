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
    extract_youtube_query,
    shutdown_pc,
    restart_pc,
    take_screenshot,
    decrease_brightness,
    increase_brightness,
    set_brightness
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
    "decrease_brightness": decrease_brightness,
    "increase_brightness": increase_brightness,
    "set_brightness": set_brightness,
    "list_directory": list_directory,
    "read_file": read_file,
    "write_file": write_file,
    "create_directory": create_directory,
    "delete_path": delete_path,
    "search_files": search_files
}


def jarvis_agent(state: AgentState):

    user_input = state["user_input"].lower()

    memory = state.get("conversation_history", [])

    responses = []

    # ==========================================
    # OPEN APPS
    # ==========================================

    if "open" in user_input:

        if "chrome" in user_input:
            responses.append(open_chrome())

        if "vscode" in user_input or "visual studio" in user_input:
            responses.append(open_vscode())

        if "youtube" in user_input:
            responses.append(open_youtube())

        if "whatsapp" in user_input:
            responses.append(open_whatsapp())

    # ==========================================
    # YOUTUBE SEARCH/PLAY
    # ==========================================

    if "youtube" in user_input and any(
        w in user_input
        for w in ["play", "search", "find"]
    ):

        query = extract_youtube_query(user_input)

        if query:
            responses.append(search_youtube(query))
        else:
            responses.append(open_youtube())

    # ==========================================
    # GOOGLE SEARCH
    # ==========================================

    if "search" in user_input:

        query = user_input.replace("search", "").replace("for", "").strip()

        if "google" in user_input:
            query = query.replace("google", "").strip()

        if query:
            responses.append(search_google(query))
        else:
            responses.append("What should I search for?")

    # ==========================================
    # SCREENSHOT
    # ==========================================

    if "screenshot" in user_input:
        responses.append(take_screenshot())

    # ==========================================
    # BRIGHTNESS
    # ==========================================

    if "brightness" in user_input:

        if "decrease" in user_input or "lower" in user_input or "dim" in user_input:
            responses.append(decrease_brightness())

        elif "increase" in user_input or "raise" in user_input or "brighten" in user_input:
            responses.append(increase_brightness())

        else:
            # Try to extract number
            import re
            numbers = re.findall(r'\d+', user_input)
            if numbers:
                responses.append(set_brightness(int(numbers[0])))
            else:
                responses.append("Specify brightness level (0-100)")

    # ==========================================
    # SHUTDOWN/RESTART
    # ==========================================

    if "shutdown" in user_input or "turn off" in user_input:
        responses.append(shutdown_pc())

    if "restart" in user_input or "reboot" in user_input:
        responses.append(restart_pc())

    # ==========================================
    # FILE OPERATIONS
    # ==========================================

    if "list" in user_input or "show files" in user_input:
        responses.append(list_directory())

    if "read" in user_input or "open file" in user_input:
        # Extract filename
        words = user_input.split()
        for i, w in enumerate(words):
            if w in ["read", "file", "open"] and i + 1 < len(words):
                responses.append(read_file(words[i + 1]))
                break

    # ==========================================
    # IF NO COMMAND MATCHED, USE LLM
    # ==========================================

    if not responses:

        prompt = f"""
User: {user_input}

Provide a helpful response.
"""

        response = ask_llm(prompt)
        responses.append(str(response))

    # Combine responses
    final_response = "\n".join(responses)

    # Update memory
    memory.append({"role": "user", "content": state["user_input"]})
    memory.append({"role": "assistant", "content": final_response})

    return {
        "response": final_response,
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
