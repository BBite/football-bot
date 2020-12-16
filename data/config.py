import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admins = [
    os.getenv("ADMIN_ID_1"),
    os.getenv("ADMIN_ID_2"),
]

ip = os.getenv("ip")

I18N_DOMAIN = 'football-bot'
BASE_DIR = Path(__file__).parent.parent
LOCALES_DIR = BASE_DIR / 'locales'
