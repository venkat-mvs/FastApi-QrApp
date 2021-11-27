from typing import Optional
from pydantic import BaseSettings
from functools import lru_cache

class Env(BaseSettings):
    
    qrcodeversion:Optional[int] = 1

    class Config:
        env_file = ".env"

class ENV:
    @lru_cache
    def values() -> Env:
        return Env()



# @lru_cache
# def GetEnvironments() -> Env:
#     return Env()