from loguru import logger
import sys

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
)

logger.add(
    "logs/devpulse.log",
    rotation="10 MB",
    retention="30 days",
    level="INFO",
)

__all__ = ["logger"]