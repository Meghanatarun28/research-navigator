from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):
    ollama_model: str = "qwen3:8b"

    qdrant_host: str = "localhost"

    qdrant_port: int = 6333

    refusal_threshold: float = 0.70

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
