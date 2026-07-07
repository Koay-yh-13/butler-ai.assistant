from pathlib import Path
from pydantic import BaseModel
import os


class ButlerConfig(BaseModel):
    assistant_name: str = "Butler"
    version: str = "0.1.0"

    openrouter_api_key: str = ""
    model: str = "openai/gpt-5"

    host: str = "127.0.0.1"
    port: int = 8000

    memory_folder: str = "memory"
    log_folder: str = "logs"


BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG = ButlerConfig(
    openrouter_api_key=os.getenv("OPENROUTER_API_KEY", "")
)
