from graph.state import AgentState

from tools.system_tools import (
    search_google,
    open_youtube
)


def browser_agent(state: AgentState):

    user_input = state["user_input"].lower()

    response = "Browser command not recognized"

    if "youtube" in user_input:

        response = open_youtube()

    elif "search" in user_input:

        query = user_input.replace(
            "search",
            ""
        ).strip()

        response = search_google(query)

    return {
        "response": response
    }