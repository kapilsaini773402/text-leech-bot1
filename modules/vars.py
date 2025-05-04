import os

API_ID    = os.environ.get("API_ID", "20351304")
API_HASH  = os.environ.get("API_HASH", "c09d07f9c0600cdc2f6eef07130df8e1")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7264896037:AAHZ0ABhEFDQqHPTmxk6GYtEuOLQ5SgQa6A") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8000))  # Default to 8000 if not set
