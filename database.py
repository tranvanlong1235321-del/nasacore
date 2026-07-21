import json
import os
from config import USERS_FILE


def load_users():
    """Đọc dữ liệu người chơi"""
    if not os.path.exists(USERS_FILE):
        return {}

        with open(USERS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_users(users):
    """Lưu dữ liệu người chơi"""
    with open(USERS_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4, ensure_ascii=False)
        def create_user(user):
        """Tạo người chơi mới"""

        users = load_users()

        user_id = str(user.id)

        if user_id in users:
        return False

        users[user_id] = {
        "id": user.id,
        "name": user.first_name,
        "username": user.username if user.username else "",

        "level": 1,

        "crystal": 0,
        "gem": 0,

        "total_crystal": 0,
        "weekly_crystal": 0,
        "monthly_crystal": 0,

        "ads": 0,
        "links": 0,

        "referrals": 0,

        "created_at": 0,

        "last_daily": 0,
        "last_scan": 0,

        "banned": False
    }

        save_users(users)

        return True
    def get_user(user_id):
        """Lấy thông tin người chơi"""

        users = load_users()

        return users.get(str(user_id))
    def update_user(user_id, data):
        """Cập nhật dữ liệu người chơi"""

        users = load_users()

        users[str(user_id)] = data

        save_users(users)
    def add_crystal(user_id, amount):
        """Cộng Crystal cho người chơi"""

        user = get_user(user_id)

        if not user:
            return False

            user["crystal"] += amount
            user["total_crystal"] += amount
            user["weekly_crystal"] += amount
            user["monthly_crystal"] += amount

            update_user(user_id, user)

            return True
    def remove_crystal(user_id, amount):
        """Trừ Crystal của người chơi"""

        user = get_user(user_id)

        if not user:
            return False

            if user["crystal"] < amount:
                return False

                user["crystal"] -= amount

                update_user(user_id, user)

                return True
    def add_gem(user_id, amount):

        """Cộng Gem"""

        user = get_user(user_id)

        if not user:

            return False

            user["gem"] += amount

            update_user(user_id, user)

            return True