from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7660148947:AAGH2_XFE9Ntpj9NNzr7PacO0o-GRMONvKU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Chào mừng đến với NasaCore!\n\n"
        "Bạn đã trở thành một Chỉ huy Không gian.\n"
        "Hãy sẵn sàng xây dựng căn cứ đầu tiên!"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("NasaCore Bot đang chạy...")
    app.run_polling()

if __name__ == "__main__":
    main()