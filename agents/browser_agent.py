from graph.state import AgentState

from tools.system_tools import (
    search_google,
    open_youtube,
    search_youtube
)


def browser_agent(state: AgentState):

    try:

        user_input = state["user_input"].lower()

        response = "Browser command not recognized"

        # ==========================================
        # YOUTUBE
        # ==========================================

        if "youtube" in user_input:

            # Check if want to play/search something
            if any(w in user_input for w in ["play", "search", "find"]):

                # Extract query
                query = user_input

                for word in ["play", "search", "find"]:
                    if word in query:
                        query = query.split(word)[-1].strip()
                        break

                if "youtube" in query:
                    query = query.replace("youtube", "").strip()

                response = search_youtube(query)

            else:

                response = open_youtube()

        # ==========================================
        # SEARCH GOOGLE
        # ==========================================

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