import os

class Config:

    # Telegram Bot
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    # Firebase
    FIREBASE_PROJECT_ID = os.getenv("FIREBASE_PROJECT_ID")
    FIREBASE_CLIENT_EMAIL = os.getenv("FIREBASE_CLIENT_EMAIL")
    FIREBASE_PRIVATE_KEY = os.getenv("FIREBASE_PRIVATE_KEY")

    # Bot Information
    BOT_NAME = "XPK INCOME BOT"
    BOT_VERSION = "2.0.0"

    # Currency
    CURRENCY = "৳"

    # Withdraw
    MIN_WITHDRAW = 100
    MAX_WITHDRAW = 5000
    WITHDRAW_CHARGE = 10

    # Referral
    REFERRAL_RATE = 0.05

    # Payment Days
    PAYMENT_DAYS = [10, 21, "LAST"]

    # Admin
    SUPER_ADMIN = []
