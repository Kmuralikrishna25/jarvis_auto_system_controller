import os
import re
import webbrowser
import urllib.parse

import pyautogui


def open_chrome() -> str:

    os.system("start chrome")

    return "Opening Chrome"


def open_vscode() -> str:

    os.system("code")

    return "Opening VS Code"


def open_youtube() -> str:

    webbrowser.open("https://youtube.com")

    return "Opening YouTube"


def search_google(query: str) -> str:

    url = (
        "https://www.google.com/search?q="
        + urllib.parse.quote(query)
    )

    webbrowser.open(url)

    return f"Searching Google for {query}"


def shutdown_pc() -> str:

    os.system("shutdown /s /t 5")

    return "Shutting down system"


def restart_pc() -> str:

    os.system("shutdown /r /t 5")

    return "Restarting system"


def take_screenshot() -> str:

    image = pyautogui.screenshot()

    image.save("screenshots/screenshot.png")

    return "Screenshot captured"


def open_whatsapp() -> str:

    webbrowser.open(
        "https://web.whatsapp.com"
    )

    return "Opening WhatsApp Web"


def search_youtube(query: str) -> str:

    if not query:
        query = "trending"

    url = (
        "https://www.youtube.com/results?search_query="
        + urllib.parse.quote(query)
    )

    webbrowser.open(url)

    return f"Searching YouTube for {query}"


def extract_youtube_query(user_input: str) -> str:

    # Remove common filler words (word boundary only)
    stop_words = {
        "play", "search", "find", "youtube", "on",
        "open", "and", "for", "the", "me", "a",
        "any", "some", "please", "can", "could"
    }

    words = user_input.lower().split()

    filtered = [
        w for w in words
        if w not in stop_words
    ]

    return " ".join(filtered).strip()


def set_brightness(level: int) -> str:

    try:

        import screen_brightness_control as sbc

        sbc.set_brightness(level)

        return f"Brightness set to {level}%"

    except:

        return "Failed to change brightness. Install: pip install screen-brightness-control"


def decrease_brightness(amount: int = 20) -> str:

    try:

        import screen_brightness_control as sbc

        current = sbc.get_brightness()[0]

        new_level = max(0, current - amount)

        sbc.set_brightness(new_level)

        return f"Brightness decreased to {new_level}%"

    except:

        return "Failed to change brightness. Install: pip install screen-brightness-control"


def increase_brightness(amount: int = 20) -> str:

    try:

        import screen_brightness_control as sbc

        current = sbc.get_brightness()[0]

        new_level = min(100, current + amount)

        sbc.set_brightness(new_level)

        return f"Brightness increased to {new_level}%"

    except:

        return "Failed to change brightness. Install: pip install screen-brightness-control"