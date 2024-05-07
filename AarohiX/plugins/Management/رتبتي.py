import asyncio

import random

from AarohiX import app

from pyrogram.types import (InlineKeyboardButton,

                            InlineKeyboardMarkup, Message)

from strings.filters import command

from pyrogram import filters, Client


@app.on_message(filters.command("رتبتي", ""))
async def rotba(_: Client, message: Message):
    user_id = message.from_user.id 
    member = await app.get_chat_member(message.chat.id ,user_id)
    if member.status == ChatMemberStatus.MEMBER: return await message.reply("↢ متاكد انك مشرف ؟🙄", reply_to_message_id=message.id)
    elif member.status == ChatMemberStatus.ADMINISTRATOR: return await message.reply("↢ رتبتك هي ادمن المجموعه 🖤", reply_to_message_id=message.id)
    elif member.status == ChatMemberStatus.OWNER: return await message.reply("↢ رتبتك هي مالك المجموعه 🙈", reply_to_message_id=message.id)
