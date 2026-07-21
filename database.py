import json
import os

DATABASE_FILE = "users.json"


def load_users():
    """Đọc toàn bộ dữ liệu người chơi"""

    if not os.path.exists(DATABASE_FILE):
        return {}

    with open(DATABASE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_users(users):
    """Lưu dữ liệu"""

    with open(DATABASE_FILE, "w", encoding="utf-8") as file:
        json.dump(
            users,
            file,
            indent=4,
            ensure_ascii=False
        )