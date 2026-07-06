import firebase_admin
from firebase_admin import credentials, firestore
import os

db = None

def initialize_firebase():
    global db

    if firebase_admin._apps:
        db = firestore.client()
        return db

    cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    if not cred_path:
        raise Exception("GOOGLE_APPLICATION_CREDENTIALS is not set.")

    cred = credentials.Certificate(cred_path)

    firebase_admin.initialize_app(cred)

    db = firestore.client()

    return db
