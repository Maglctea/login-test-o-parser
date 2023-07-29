import logging
import os
from logging import Logger
from logging.handlers import RotatingFileHandler
from pathlib import Path

from dotenv import load_dotenv

# Logger
logger: Logger = logging.getLogger()

logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = RotatingFileHandler('bot.log', maxBytes=2097152, backupCount=1000)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Dirs
BASE_DIR = Path(__file__).parent.parent
load_dotenv(BASE_DIR / ".env")


# TG
BOT_KEY = os.getenv("TG_KEY")
API_LINK = os.getenv("API_LINK")
ADMINS_USERNAMES = os.getenv("ADMINS_USERNAMES", "maglctea").split(',')
ADMINS_IDS = os.getenv("ADMINS_IDS", "").split(',')
MAX_ITEMS_PARSED_COUNT = os.getenv("MAX_ITEMS_PARSED_COUNT")
