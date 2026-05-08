from graph.state import AgentState

from tools.system_tools import (
    search_google,
    open_youtube
)


def browser_agent(state: AgentState):

    try:

        user_input = state["user_input"].lower()

        response = "Browser command not recognized"

        if "youtube" in user_input:

            response = open_youtube()

        elif "search" in user_input:

            # Extract query after "search" or "search for"
            if "search for" in user_input:

                query = user_input.split("search for")[-1].strip()

            else:

                query = user_input.replace(
                    "search",
                    ""
                ).strip()

            if query:
                response = search_google(query)
            else:
                response = "What should I search for?"

        return {
            "response": response
        }

    except Exception as e:

        return {
            "response": f"Error: {str(e)}"
        }

    except Exception as e:

        return {
            "response": f"Error in browser agent: {str(e)}"
        }