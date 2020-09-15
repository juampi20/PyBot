# settings.py
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# CONFIGS
PREFIX = os.environ.get("PREFIX")
# API KEYS
BOT_TOKEN = os.environ.get("BOT_TOKEN")
RIOT_API_TOKEN = os.environ.get("RIOT_API_TOKEN")
