from pydantic import BaseSettings


class Env(BaseSettings):
    
    class Config:
        env = ".env"