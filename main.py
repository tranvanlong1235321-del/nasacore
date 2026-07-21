from telegram.ext import ApplicationBuilder, CommandHandler

from config import BOT_TOKEN
from handlers import start


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("🚀 NasaCore Bot is running...")

app.run_polling()