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


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
     await message.reply_photo(
        photo=f"https://telegra.ph/file/b10503b594e3b660f5f23.jpg",
        caption=f"""**𝐓𝐡𝐢𝐬 𝐈𝐬 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 𝐑𝐮𝐧 𝐎𝐧 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐕𝐩𝐬 𝐒𝐞𝐫𝐯𝐞𝐫 𝐅𝐞𝐞𝐥 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐌𝐮𝐬𝐢𝐜 𝐈𝐧 𝐕𝐜 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 = [sky](https://t.me/susumuenakk)
        
        
𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐲 𝐁𝐨𝐬𝐬 = [sky](https://t.me/susumuenakk)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✚ Add me to your Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(" 𝐂𝐫𝐞𝐚𝐭𝐨𝐫", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton(" 𝐒𝐨𝐮𝐫𝐜𝐞 ", url=f"https://github.com/Skyy112/musicsky")
                ],[
                    InlineKeyboardButton(" 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 ", url=f"https://t.me/yaudahhlahhhh"),
                    InlineKeyboardButton(" 𝐔𝐩𝐝𝐚𝐭𝐞", url=f"https://t.me/yaudahhlahhhh")
                ],[
                    InlineKeyboardButton(" How To Use? Commands", callback_data="cb_cmd")
                ],
            ]
        ),
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(c: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("**× I am Alive ×**\n\n@yaudahhlahhhh ")


@Client.on_message(command(["repo"]) & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text("`Click on the Button given below to Get the Bot Source Code.`",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 𝐒𝐨𝐮𝐫𝐜𝐞 ", url=f"https://github.com/Skyy112/musicsky")
                ]
            ]
        ),
    )
