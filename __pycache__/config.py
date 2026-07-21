import os
from dotenv import load_dotenv

load_dotenv()

# ==========================
# TELEGRAM
# ==========================

BOT_TOKEN = os.getenv("BOT_TOKEN")

# ==========================
# ADMIN
# ==========================

ADMIN_IDS = [
    123456789
]

# ==========================
# DATA FILES
# ==========================

USERS_FILE = "data/users.json"
SETTINGS_FILE = "data/settings.json"
TRANSACTIONS_FILE = "data/transactions.json"

# ==========================
# PROJECT
# ==========================

PROJECT_NAME = "NasaCore"
VERSION = "1.0.0"