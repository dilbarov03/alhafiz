import os
from pathlib import Path

import environ
import requests

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))


def send_telegram_message(text="Text"):
    token = env.str("BOT_TOKEN")
    chat_id = env.str("CHAT_ID")

    url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=html".format(token, chat_id, text)
    response = requests.post(url)
    print(response.json())