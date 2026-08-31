# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # загружает переменные из .env

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID=os.getenv("ADMIN_ID")