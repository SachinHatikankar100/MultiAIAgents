from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    ALLOWED_PROVIDERS = [
        "Gemini",
        "Groq"
    ]
    GEMINI_MODELS = [
        "gemini-2.5-pro",
        "gemini-2.5-flash"
    ]
    GROQ_MODELS = [
    "llama-3.1-70b-versatile",
    "mixtral-8x7b-32768"
    ]


config = Config()