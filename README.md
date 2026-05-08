# Jarvis AI Assistant

A voice-controlled AI assistant for Windows PC automation powered by Google Gemini LLM.

## Features

- 🎤 Voice command recognition (say "Jarvis" wake word)
- 🗣️ Text-to-speech responses
- 🤖 Google Gemini integration for smart command processing
- 📱 Control applications (WhatsApp, Chrome, Spotify, etc.)
- 🔊 System controls (volume, brightness)
- 📸 Screenshot capture
- 🤖 Automation tasks

## Project Structure

```
jarvis/
├── main.py           # Entry point
├── config.py         # Configuration settings
├── requirements.txt   # Dependencies
├── modules/          # Core modules
│   ├── voice.py      # Speech recognition & TTS
│   ├── ai_brain.py   # Google Gemini integration
│   ├── commands.py   # Command execution
│   ├── automation.py # Automation tasks
│   └── utils.py      # Utility functions
├── memory/           # Memory storage
├── sounds/           # Sound files
└── screenshots/      # Screenshot storage
```

## Setup

1. Create virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate virtual environment:
   ```bash
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies:
   ```bash
   pip install -r jarvis/requirements.txt
   ```

4. Configure environment variables in `.env`:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   WAKE_WORD=jarvis
   MICROPHONE_INDEX=5
   ```

## Usage

Run Jarvis:
```bash
python -m jarvis.main
```

Choose mode:
- **voice** - Say "Jarvis" followed by your command
- **text** - Type commands directly

## Example Commands

- "Jarvis, open WhatsApp"
- "Jarvis, volume up"
- "Jarvis, take screenshot"
- "Jarvis, brightness down"

## License

MIT
