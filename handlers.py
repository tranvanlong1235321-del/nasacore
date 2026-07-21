from telegram import Update
from telegram.ext import ContextTypes

from database import load_users, save_users


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    users = load_users()

    user_id = str(user.id)

    if user_id not in users:

        users[user_id] = {
            "name": user.first_name,
            "username": user.username,
            "level": 1,
            "crystal": 0,
            "gem": 0
        }

        save_users(users)

        await update.message.reply_text(
            f"""🚀 Chào mừng {user.first_name}!

Tài khoản NasaCore đã được tạo.

⭐ Level: 1
💎 Gem: 0
🔷 Crystal: 0
"""
        )

    else:

        player = users[user_id]

        await update.message.reply_text(
            f"""👋 Chào mừng quay lại!

👤 {player["name"]}

⭐ Level: {player["level"]}

💎 Gem: {player["gem"]}

🔷 Crystal: {player["crystal"]}
"""
        )