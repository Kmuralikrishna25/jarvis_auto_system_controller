# Jarvis AI Assistant

A voice-controlled AI assistant for Windows PC automation powered by Google Gemini LLM with real-time web data.

## Features

- 🎤 Voice command recognition
- 🗣️ Text-to-speech responses (Windows SAPI)
- 🤖 Google Gemini integration for smart command processing
- 📱 Control applications (Chrome, VS Code, WhatsApp, YouTube)
- 🔊 System controls (brightness, shutdown, restart)
- 📸 Screenshot capture
- 📁 File operations (read, write, list, search)
- 🔔 Reminders and scheduling
- 🧠 Persistent conversation memory
- ⏹️ ESC key to stop speech anytime
- 🌐 Wikipedia search (free, no key)
- 🔍 Google Search via SerpAPI
- 🌡️ Weather reports via OpenWeatherMap
- 📰 Latest news via NewsAPI

## Project Structure

```
jarvis_auto_system_controller/
├── main.py               # Entry point
├── config.py             # Configuration (Gemini model, API key)
├── requirements.txt      # Dependencies
├── .env                  # Environment variables (API keys)
├── agents/               # Agent modules
│   ├── voice_agent.py    # Speech recognition & TTS
│   ├── browser_agent.py  # Web search & YouTube
│   ├── coding_agent.py   # Programming assistance
│   ├── system_agent.py   # System commands
│   ├── memory_agent.py   # Conversation memory
│   └── file_agent.py     # File operations
├── graph/                # LangGraph workflow
│   ├── builder.py        # Graph compilation
│   ├── state.py          # Agent state types
│   └── supervisor.py     # Task routing
├── tools/                # Tool functions
│   ├── ai_tools.py       # Gemini LLM interface
│   ├── system_tools.py   # System control (apps, brightness, etc.)
│   ├── file_tools.py     # File operations
│   ├── memory_tools.py   # Memory storage
│   ├── scheduler_tools.py# Reminders & scheduling
│   └── web_tools.py      # Wikipedia, SerpAPI, Weather, News
├── memory/               # Conversation history storage
└── screenshots/          # Screenshot storage
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
   pip install -r requirements.txt
   ```

4. Configure `.env` file:
   ```
   GOOGLE_API_KEY=your_gemini_api_key_here
   MODEL_NAME=gemini-2.0-flash
   MICROPHONE_INDEX=0
   
   # Optional: Get free keys from respective websites
   SERPAPI_KEY=your_key      # https://serpapi.com (100 free/month)
   WEATHER_API_KEY=your_key  # https://openweathermap.org
   NEWSAPI_KEY=your_key      # https://newsapi.org (100 reqs/day)
   ```

   Get a free Gemini API key: https://makersuite.google.com/app/apikey

## Usage

Run Jarvis:
```bash
python main.py
```

Jarvis will say "Welcome boss" and start listening.

## Example Commands

- "Open Chrome"
- "Open YouTube and play python tutorial"
- "Search Google for weather"
- "Open WhatsApp"
- "Take screenshot"
- "Decrease brightness"
- "Shutdown" or "Restart"
- "Remind me in 5 minutes to check email"
- "List files"
- "Read myfile.txt"
- "Exit" - says "Ok boss, have a nice day"

## Controls

- **Say "stop"** while Jarvis is speaking to stop mid-sentence
- **Press ESC** to stop speech immediately
- Ask a new question while Jarvis answers to switch topics

## License

MIT
