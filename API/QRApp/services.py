from functools import lru_cache

from .QRGenerator import QRGenerator

@lru_cache
async def QRGeneratorService() -> QRGenerator:
    return QRGenerator()