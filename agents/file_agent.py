from graph.state import AgentState

from tools.file_tools import (
    list_directory,
    read_file,
    write_file,
    create_directory,
    delete_path,
    search_files
)

from tools.ai_tools import ask_llm


def file_agent(state: AgentState):

    try:

        user_input = state["user_input"].lower()

        # ==========================================
        # LIST DIRECTORY
        # ==========================================

        if "list" in user_input or "show files" in user_input:

            path = "."

            if "in" in user_input:
                parts = user_input.split("in")
                if len(parts) > 1:
                    path = parts[1].strip()

            return {"response": list_directory(path)}

        # ==========================================
        # READ FILE
        # ==========================================

        if "read" in user_input or "open file" in user_input:

            words = user_input.split()

            filepath = None

            for i, word in enumerate(words):
                if word in ["read", "file", "open"] and i + 1 < len(words):
                    filepath = words[i + 1]
                    break

            if filepath:
                return {"response": read_file(filepath)}

            return {"response": "Please specify a file to read."}

        # ==========================================
        # CREATE DIRECTORY
        # ==========================================

        if "create directory" in user_input or "make folder" in user_input:

            words = user_input.split()

            dirname = None

            for i, word in enumerate(words):
                if word in ["directory", "folder"] and i + 1 < len(words):
                    dirname = words[i + 1]
                    break

            if dirname:
                return {"response": create_directory(dirname)}

            return {"response": "Please specify directory name."}

        # ==========================================
        # SEARCH FILES
        # ==========================================

        if "search for" in user_input or "find files" in user_input:

            words = user_input.split()

            pattern = "*.py"

            if "for" in user_input:
                pattern = user_input.split("for")[-1].strip()

            return {"response": search_files(pattern)}

        # ==========================================
        # DEFAULT: ASK LLM
        # ==========================================

        prompt = f"""
You are Jarvis's file management system.

User request: {user_input}

Available tools:
- list_directory
- read_file
- write_file
- create_directory
- delete_path
- search_files

Provide a helpful response about file operations.
"""

        response = ask_llm(prompt)

        return {"response": response}

    except Exception as e:

        return {"response": f"Error in file agent: {str(e)}"}
