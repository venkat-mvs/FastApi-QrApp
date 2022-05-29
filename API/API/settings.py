from pydantic import BaseSettings
from functools import lru_cache
import os, pathlib

BASE_DIR = pathlib.Path(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

class Env(BaseSettings):

    HOST: str = "localhost" 
    PORT: int = 8000
    API_TITLE: str 
    API_VERSION: str

    class Config:
        env_file = BASE_DIR / ".env"

class ENV:
    @lru_cache
    def values() -> Env:
        return Env()
