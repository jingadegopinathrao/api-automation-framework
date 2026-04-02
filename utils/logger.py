from loguru import logger
import sys
import os

# Create logs folder
os.makedirs("logs", exist_ok=True)

# Remove default logger
logger.remove()

# Console logging
logger.add(
    sys.stdout,
    level="INFO",
    format="<green>{time}</green> | <level>{level}</level> | <cyan>{message}</cyan>"
)

# File logging
logger.add(
    "logs/api_tests.log",
    rotation="1 MB",
    retention="7 days",
    level="DEBUG"
)