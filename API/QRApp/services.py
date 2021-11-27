from functools import lru_cache

from .QRGenerator import QRGenerator

@lru_cache
def QRGeneratorService() -> QRGenerator:
    return QRGenerator()