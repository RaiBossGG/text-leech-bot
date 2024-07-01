import os

API_ID    = os.environ.get("API_ID", "27872876")
API_HASH  = os.environ.get("API_HASH", "e054268dfaf066e6d19d83bab5928bf3")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7241830807:AAGUcffEd70eglHE-quD4Fx7TYIKsH1cjV4") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
