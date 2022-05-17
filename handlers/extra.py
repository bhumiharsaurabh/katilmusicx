import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import (
    BOT_USERNAME,
    OWNER_USERNAME,   
)


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text("**𝐓𝐇𝐀𝐍𝐊𝐒 𝐅𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐄 𝐈𝐍 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𝐍𝐎𝐖 𝐏𝐑𝐎𝐌𝐎𝐓𝐄 𝐌𝐄 𝐀𝐒 𝐀𝐃𝐌𝐈𝐍𝐈𝐒𝐓𝐑𝐀𝐓𝐎𝐑 𝐈𝐍 𝐓𝐇𝐈𝐒 𝐂𝐇𝐀𝐓 𝐖𝐈𝐓𝐇 𝐍𝐄𝐄𝐃𝐄𝐃 𝐏𝐎𝐖𝐄𝐑 𝐎𝐓𝐇𝐄𝐑𝐖𝐈𝐒𝐄 𝐈 𝐀𝐌 𝐍𝐎𝐓 𝐀𝐁𝐋𝐄 𝐓𝐎 𝐖𝐎𝐑𝐊 𝐏𝐑𝐎𝐏𝐄𝐑𝐋𝐘 !!**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙️ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐎𝐃𝐄", url=f"https://github.com/Skyy112/musicsky")
                ],[
                    InlineKeyboardButton("📨 𝐆𝐑𝐎𝐔𝐏", url=f"https://t.me/yaudahhlahhhh"),
                    InlineKeyboardButton("📨 𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=f"https://t.me/yaudahhlahhhh")
                  ],
            ]
        ),
    )
