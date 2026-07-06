import os
import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore


db = None


def initialize_firebase():
    global db

    if firebase_admin._apps:
        db = firestore.client()
        return db

    private_key = os.getenv("FIREBASE_PRIVATE_KEY")

    if private_key:
        private_key = private_key.replace("\\n", "\n")

    cred = credentials.Certificate({
        "type": "service_account",
        "project_id": os.getenv("FIREBASE_PROJECT_ID"),
        "private_key": private_key,
        "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
        "token_uri": "https://oauth2.googleapis.com/token"
    })

    firebase_admin.initialize_app(cred)

    db = firestore.client()

    return db
