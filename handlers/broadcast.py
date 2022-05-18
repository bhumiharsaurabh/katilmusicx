# Copyright (C) 2022 By KATIL
# Originally written by levina on github
# Broadcast function


import asyncio

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from callsmusic.callsmusic import client as katil
from config import SUDO_USERS

@Client.on_message(filters.command(["gcast"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`𝚜𝚝𝚊𝚛𝚝𝚒𝚗𝚐 𝚋𝚛𝚘𝚊𝚍𝚌𝚊𝚜𝚝 ...`")
        if not message.reply_to_message:
            await wtf.edit("**__𝚙𝚕𝚎𝚊𝚜𝚎 𝚛𝚎𝚙𝚕𝚊𝚢 𝚝𝚘 𝚊 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚝𝚘 𝚋𝚛𝚘𝚊𝚍𝚌𝚊𝚜𝚝 ...__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`𝚋𝚛𝚘𝚊𝚍𝚌𝚊𝚜𝚝` \n\n**Send To:** `{sent}` Chats \n**Failed in:** {failed} chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`gcast succesfully` \n\n**sent to:** `{sent}` chats \n**failed in:** {failed} chats")
