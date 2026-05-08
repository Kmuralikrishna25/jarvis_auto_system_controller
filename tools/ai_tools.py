from langchain_google_genai import ChatGoogleGenerativeAI

from config import (
    GEMINI_API_KEY,
    MODEL_NAME,
    TEMPERATURE
)

llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    google_api_key=GEMINI_API_KEY,
    temperature=TEMPERATURE
)


def ask_llm(prompt: str) -> str:
    """
    Send prompt to Gemini model
    and return response text.
    """

    response = llm.invoke(prompt)

    return response.content