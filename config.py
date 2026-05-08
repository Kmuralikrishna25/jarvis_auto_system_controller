"""Configuration management for Jarvis."""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Jarvis configuration settings."""

    def __init__(self):
        self.wake_word = os.getenv("WAKE_WORD", "jarvis")
        self.voice_rate = int(os.getenv("VOICE_RATE", 200))
        self.voice_volume = float(os.getenv("VOICE_VOLUME", 1.0))
        self.energy_threshold = int(os.getenv("ENERGY_THRESHOLD", 1000))
        self.microphone_index = int(os.getenv("MICROPHONE_INDEX", 5))
        self.gemini_api_key = os.getenv("GEMINI_API_KEY", "")
        self.supported_apps = {
            "whatsapp": "shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App",
            "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            "edge": "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
            "spotify": "spotify:",
        }
        self.memory_path = "memory/"
        self.sounds_path = "sounds/"
        self.screenshots_path = "screenshots/"

    def get(self, key, default=None):
        """Get a configuration value."""
        return getattr(self, key, default)
