from graph.state import AgentState

from tools.system_tools import (
    open_chrome,
    open_vscode,
    open_youtube,
    search_google,
    shutdown_pc,
    restart_pc,
    take_screenshot
)


def system_agent(state: AgentState):

    user_input = state["user_input"].lower()

    response = "System command not recognized"

    if "chrome" in user_input:
        response = open_chrome()

    elif "vscode" in user_input or "visual studio" in user_input:
        response = open_vscode()

    elif "youtube" in user_input:
        response = open_youtube()

    elif "search" in user_input:
        query = user_input.replace("search", "").strip()
        response = search_google(query)

    elif "shutdown" in user_input or "turn off" in user_input:
        response = shutdown_pc()

    elif "restart" in user_input or "reboot" in user_input:
        response = restart_pc()

    elif "screenshot" in user_input:
        response = take_screenshot()

    return {
        "response": response
    }
