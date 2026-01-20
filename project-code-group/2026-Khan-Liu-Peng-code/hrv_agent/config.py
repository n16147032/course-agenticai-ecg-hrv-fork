import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration for Gemini API and agent settings"""
    
    # API Key Retrieval Methods (Dynamic to pick up UI changes)
    @classmethod
    def get_openrouter_key(cls):
        return os.getenv('OPENROUTER_API_KEY', cls._get_env_or_default('OPENROUTER_API_KEY', ''))

    @staticmethod
    def _get_env_or_default(key, default):
        return os.getenv(key, default)

    # OpenRouter Settings
    OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
    OPENROUTER_MODEL = "deepseek/deepseek-v3.2"
    
    # Generation settings
    TEMPERATURE = float(os.getenv('TEMPERATURE', '0.7'))
    MAX_OUTPUT_TOKENS = int(os.getenv('MAX_OUTPUT_TOKENS', '2048'))
    
    # Remove Safety settings as they are Gemini-specific
    
    @classmethod
    def is_openrouter_available(cls):
        """Check if OpenRouter API key is configured"""
        val = os.getenv('OPENROUTER_API_KEY', '')
        return bool(val and val.strip())
