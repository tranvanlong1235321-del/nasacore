import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

ADMIN_IDS = [
    123456789
]

USERS_FILE = "data/users.json"
SETTINGS_FILE = "data/settings.json"
TRANSACTIONS_FILE = "data/transactions.json"

PROJECT_NAME = "NasaCore"
VERSION = "1.0.0"