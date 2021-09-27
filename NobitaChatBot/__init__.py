import os

from pyrogram import Client

API_ID = os.environ.get("API_ID", 2329393)
API_HASH = os.environ.get("API_HASH", "97edb95abc9a61fecea49ef8b31de8f3")
TOKEN = os.environ.get("TOKEN", "2037975975:AAEm__YIo_6W1rSXXag23DsstoCX2mbB07w")

Nobita = Client(":memory:", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)