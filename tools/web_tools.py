import requests
import wikipediaapi
import os
from typing import Optional


# ==========================================
# WIKIPEDIA API
# ==========================================

wiki = wikipediaapi.Wikipedia(
    language="en",
    user_agent="JarvisAssistant/1.0"
)


def search_wikipedia(query: str, sentences: int = 3) -> str:

    try:

        page = wiki.page(query)

        if not page.exists():
            return f"No Wikipedia article found for '{query}'"

        summary = page.summary[:sentences * 200]

        return f"Wikipedia: {summary}"

    except Exception as e:

        return f"Wikipedia error: {str(e)}"


# ==========================================
# SERPAPI (GOOGLE SEARCH)
# ==========================================

def search_serpapi(query: str) -> str:

    api_key = os.getenv("SERPAPI_KEY", "")

    if not api_key:
        return "SerpAPI key not set. Add SERPAPI_KEY to .env"

    try:

        url = "https://serpapi.com/search"

        params = {
            "q": query,
            "api_key": api_key,
            "num": 3
        }

        response = requests.get(url, params=params, timeout=10)

        data = response.json()

        results = data.get("organic_results", [])

        if not results:
            return f"No search results for '{query}'"

        output = f"Search results for '{query}':\n"

        for i, r in enumerate(results[:3], 1):
            title = r.get("title", "")
            snippet = r.get("snippet", "")
            output += f"{i}. {title}: {snippet}\n"

        return output.strip()

    except Exception as e:

        return f"Search error: {str(e)}"


# ==========================================
# WEATHER API (OpenWeatherMap)
# ==========================================

def get_weather(city: str) -> str:

    api_key = os.getenv("WEATHER_API_KEY", "")

    if not api_key:
        return "Weather API key not set. Add WEATHER_API_KEY to .env"

    try:

        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }

        response = requests.get(url, params=params, timeout=10)

        data = response.json()

        if data.get("cod") != 200:
            return f"City '{city}' not found"

        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        city_name = data["name"]

        return (
            f"Weather in {city_name}: {desc}, "
            f"Temperature: {temp}°C (feels like {feels}°C), "
            f"Humidity: {humidity}%, Wind: {wind} m/s"
        )

    except Exception as e:

        return f"Weather error: {str(e)}"


# ==========================================
# NEWS API
# ==========================================

def get_news(topic: str = "latest") -> str:

    api_key = os.getenv("NEWSAPI_KEY", "")

    if not api_key:
        return "NewsAPI key not set. Add NEWSAPI_KEY to .env"

    try:

        url = "https://newsapi.org/v2/everything"

        params = {
            "q": topic,
            "api_key": api_key,
            "pageSize": 5,
            "language": "en",
            "sortBy": "publishedAt"
        }

        response = requests.get(url, params=params, timeout=10)

        data = response.json()

        articles = data.get("articles", [])

        if not articles:
            return f"No news found for '{topic}'"

        output = f"Latest news about {topic}:\n"

        for i, a in enumerate(articles[:5], 1):
            title = a.get("title", "")
            source = a.get("source", {}).get("name", "")
            output += f"{i}. [{source}] {title}\n"

        return output.strip()

    except Exception as e:

        return f"News error: {str(e)}"
