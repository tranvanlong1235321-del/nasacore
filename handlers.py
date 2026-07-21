from telegram import Update
from telegram.ext import ContextTypes

from database import create_user, get_user


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    telegram_user = update.effective_user

    # Tạo tài khoản nếu chưa có
    created = create_user(telegram_user)

    user = get_user(telegram_user.id)

    if created:
        message = f"""
🚀 Chào mừng {user['name']} đến với NasaCore!

🎉 Tài khoản của bạn đã được tạo thành công.

⭐ Level: {user['level']}
💎 Crystal: {user['crystal']}
💰 Gem: {user['gem']}

Chúc bạn có những chuyến khám phá không gian thú vị!
"""

    else:
        message = f"""
👋 Chào mừng trở lại {user['name']}!

⭐ Level: {user['level']}
💎 Crystal: {user['crystal']}
💰 Gem: {user['gem']}
"""

    await update.message.reply_text(message)