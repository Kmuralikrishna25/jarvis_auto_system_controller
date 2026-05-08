import os
import json
import shutil
from pathlib import Path


def list_directory(path: str = ".") -> str:

    try:

        items = os.listdir(path)

        result = f"Contents of {path}:\n"

        for item in sorted(items):

            full_path = os.path.join(path, item)

            if os.path.isdir(full_path):
                result += f"[DIR] {item}\n"
            else:
                result += f"[FILE] {item}\n"

        return result.strip()

    except Exception as e:
        return f"Error listing directory: {str(e)}"


def read_file(filepath: str) -> str:

    try:

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if len(content) > 2000:
            return content[:2000] + "\n... (truncated)"

        return content

    except Exception as e:
        return f"Error reading file: {str(e)}"


def write_file(filepath: str, content: str) -> str:

    try:

        os.makedirs(
            os.path.dirname(filepath),
            exist_ok=True
        )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        return f"File saved: {filepath}"

    except Exception as e:
        return f"Error writing file: {str(e)}"


def create_directory(path: str) -> str:

    try:

        os.makedirs(path, exist_ok=True)

        return f"Directory created: {path}"

    except Exception as e:
        return f"Error creating directory: {str(e)}"


def delete_path(path: str) -> str:

    try:

        if os.path.isdir(path):
            shutil.rmtree(path)
            return f"Directory deleted: {path}"

        elif os.path.isfile(path):
            os.remove(path)
            return f"File deleted: {path}"

        else:
            return f"Path not found: {path}"

    except Exception as e:
        return f"Error deleting: {str(e)}"


def search_files(pattern: str, path: str = ".") -> str:

    try:

        matches = list(Path(path).rglob(pattern))

        if not matches:
            return f"No files matching '{pattern}' found."

        result = f"Found {len(matches)} file(s):\n"

        for match in matches[:20]:
            result += f"{match}\n"

        return result.strip()

    except Exception as e:
        return f"Error searching: {str(e)}"
