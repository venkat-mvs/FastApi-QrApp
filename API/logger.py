import logging


logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

log = logging.getLogger("QRApp")