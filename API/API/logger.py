import logging
from .settings import BASE_DIR

LOGGINGCONFIG = BASE_DIR / "logging.conf"


logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

logger = logging.getLogger("QRApp")