import os

class Config:
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    TOKEN = os.environ.get("TOKEN", "")
    START_PIC = os.environ.get("START_PIC", "")
    CHAT = os.environ.get("CHAT", "")