from graph.state import AgentState

from tools.system_tools import (
    open_chrome,
    open_vscode,
    open_youtube,
    open_whatsapp,
    search_google,
    shutdown_pc,
    restart_pc,
    take_screenshot
)


def system_agent(state: AgentState):

    user_input = state["user_input"].lower()

    try:

        # ==========================================
        # OPEN CHROME
        # ==========================================

        if "chrome" in user_input:

            return {
                "response": open_chrome()
            }

        # ==========================================
        # OPEN VSCODE
        # ==========================================

        elif "vscode" in user_input:

            return {
                "response": open_vscode()
            }

        # ==========================================
        # OPEN YOUTUBE
        # ==========================================

        elif "youtube" in user_input:

            return {
                "response": open_youtube()
            }

        # ==========================================
        # OPEN WHATSAPP
        # ==========================================

        elif "whatsapp" in user_input:

            return {
                "response": open_whatsapp()
            }

        # ==========================================
        # GOOGLE SEARCH
        # ==========================================

        elif "search google" in user_input:

            query = user_input.replace(
                "search google",
                ""
            ).strip()

            return {
                "response": search_google(query)
            }

        # ==========================================
        # SHUTDOWN
        # ==========================================

        elif "shutdown" in user_input:

            return {
                "response": shutdown_pc()
            }

        # ==========================================
        # RESTART
        # ==========================================

        elif "restart" in user_input:

            return {
                "response": restart_pc()
            }

        # ==========================================
        # SCREENSHOT
        # ==========================================

        elif "screenshot" in user_input:

            return {
                "response": take_screenshot()
            }

        # ==========================================
        # DEFAULT
        # ==========================================

        return {
            "response": "System command not recognized"
        }

    except Exception as e:

        return {
            "response": f"Error executing command: {str(e)}"
        }