import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app
from asyncio import gather

 
@app.on_message(filters.command(["تحويل الي صوره", "تحويل الملصق"], ""))
async def sticker_image(client: Client, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("↢ قم بالرد علي الملصق")
    if not reply.sticker:
        return await message.reply("↢ قم بالرد علي الصوره")
    m = await message.reply("↢ انتظر حتي يتم صنع الصوره 🕜")
    f = await reply.download(f"{reply.sticker.file_unique_id}.png")
    await gather(*[message.reply_photo(f),message.reply_document(f)], "")
    await m.delete()
    os.remove(f)

