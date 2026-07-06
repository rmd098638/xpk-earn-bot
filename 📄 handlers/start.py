from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        ["📤 File Submit"],
        ["👤 Profile", "💼 Wallet"],
        ["💸 Withdraw", "👥 Referral"],
        ["📜 Rules", "📊 Statement"],
        ["📞 Support", "📢 Channels"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "🌺 আসসালামু আলাইকুম! 🌺\n\n"
        "🎉 Welcome to XPK INCOME BOT\n\n"
        "👨‍💼 Main Admin: @jobayer2010\n\n"
        "💖 আপনাকে আমাদের অফিসিয়াল বটে স্বাগতম।\n\n"
        "👇 নিচের মেনু থেকে একটি অপশন নির্বাচন করুন।",
        reply_markup=reply_markup
    )
