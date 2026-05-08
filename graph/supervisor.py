from graph.state import AgentState


SYSTEM_KEYWORDS = [
    "open",
    "shutdown",
    "restart",
    "screenshot",
    "chrome",
    "vscode"
]

BROWSER_KEYWORDS = [
    "search",
    "youtube",
    "google"
]

CODING_KEYWORDS = [
    "code",
    "python",
    "bug",
    "function",
    "program"
]


def supervisor(state: AgentState):

    user_input = state["user_input"].lower()

    if any(
        keyword in user_input
        for keyword in SYSTEM_KEYWORDS
    ):

        return {
            "next_agent": "system_agent"
        }

    if any(
        keyword in user_input
        for keyword in BROWSER_KEYWORDS
    ):

        return {
            "next_agent": "browser_agent"
        }

    if any(
        keyword in user_input
        for keyword in CODING_KEYWORDS
    ):

        return {
            "next_agent": "coding_agent"
        }

    return {
        "next_agent": "coding_agent"
    }