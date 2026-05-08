import os
import webbrowser
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

    webbrowser.open(
        f"https://www.google.com/search?q={query}"
    )

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