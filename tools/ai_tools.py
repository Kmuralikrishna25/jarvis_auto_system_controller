from langchain_ollama import ChatOllama

from config import (
    OLLAMA_MODEL,
    TEMPERATURE
)

llm = ChatOllama(
    model=OLLAMA_MODEL,
    temperature=TEMPERATURE
)


def ask_llm(prompt: str) -> str:
    """
    Send prompt to Ollama model
    and return response.
    """

    response = llm.invoke(prompt)

    return response.content