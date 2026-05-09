import os
from dotenv import load_dotenv

load_dotenv()

# ==============================
# GEMINI CONFIGURATION
# ==============================

GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY", "")

MODEL_NAME = os.getenv("MODEL_NAME", "gemini-1.5-flash")

TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))


# ==============================
# SYSTEM CONFIGURATION
# ==============================

SCREENSHOT_DIR = "screenshots"

MEMORY_PATH = "memory/chat_history.json"