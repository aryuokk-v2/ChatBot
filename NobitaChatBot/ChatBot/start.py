from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from NobitaChatBot import Nobita

NOBITA_START = """
I am Nobita, An Intelligent ChatBot.[⠀](https://telegra.ph/file/7ab6d51c24bef8396b752.png)
"""


@Nobita.on_message(
    filters.command(["start"], prefixes=["/", "!"]) & ~filters.edited)
async def info(client, message):
    buttons = [
        [
            InlineKeyboardButton(
                "Developer",
                url="https://t.me/its_Prince"),
            InlineKeyboardButton("Join",
                                 url="https://t.me/HaramiSquad"),
            InlineKeyboardButton("Updates",
                                 url="https://t.me/roBots_Hub"),
        ],
    ]
    await Nobita.send_message(
        chat_id=message.chat.id,
        text=NOBITA_START,
        reply_markup=InlineKeyboardMarkup(buttons),
    )
