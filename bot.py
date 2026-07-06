from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from config import Config
from firebase import initialize_firebase


# ==========================
# START COMMAND
# ==========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🌺 আসসালামু আলাইকুম!\n\n"
        "🎉 Welcome to XPK INCOME BOT\n\n"
        "✅ Bot Started Successfully."
    )


# ==========================
# MAIN
# ==========================
def main():

    # Firebase
    initialize_firebase()

    # Telegram Bot
    app = Application.builder().token(
        Config.BOT_TOKEN
    ).build()

    # Commands
    app.add_handler(CommandHandler("start", start))

    print("✅ XPK INCOME BOT Started")

    app.run_polling()


if __name__ == "__main__":
    main()
