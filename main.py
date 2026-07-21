from telegram.ext import Application, CommandHandler

from handlers import start

TOKEN = "7660148947:AAGH2_XFE9Ntpj9NNzr7PacO0o-GRMONvKU"


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("🚀 NasaCore đang chạy...")

    app.run_polling()


if __name__ == "__main__":
    main()