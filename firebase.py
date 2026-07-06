import os
import firebase_admin
from firebase_admin import credentials, firestore

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
        "private_key_id": "",
        "private_key": private_key,
        "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
        "client_id": "",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": ""
    })

    firebase_admin.initialize_app(cred)

    db = firestore.client()

    return db
