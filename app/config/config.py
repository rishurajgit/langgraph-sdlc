from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # GEMINI_API_KEY: str
    # GEMINI_MODEL: str
    # GROQ_API_KEY: str
    # GROQ_MODEL: str
    OPENROUTER_API_KEY: str
    OPENROUTER_MODEL: str
    
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
    
settings = Settings()