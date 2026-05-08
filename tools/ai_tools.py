from langchain_ollama import ChatOllama

from config import (
    OLLAMA_MODEL,
    TEMPERATURE
)


llm = ChatOllama(
    model=OLLAMA_MODEL,
    temperature=TEMPERATURE
)


def ask_llm(prompt: str, history: list = None) -> str:

    try:

        response = llm.invoke(prompt)

        return response.content

    except Exception as e:

        return f"Error: {str(e)}"
