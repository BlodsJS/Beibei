import os
from pathlib import Path

from discord import Intents
from dotenv import load_dotenv

load_dotenv()

# bot token
TOKEN = os.getenv("DISCORD_TOKEN")
# bot prefix
PREFIXES = ["b!", "B!"]

# basic configs (commands)
INTENTS = Intents.default()
INTENTS.message_content = True
INTENTS.members = True

# ia token
# AI_TOKEN = os.getenv("AI_API_KEY")
# PERSONALITY_FILE = "pers_bei.txt"
ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
LOG_DIR = ROOT_DIR / "logs"
DB_PATH = DATA_DIR / "bot.db"
