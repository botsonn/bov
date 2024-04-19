import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app
from asyncio import gather
from pyrogram.errors import FloodWait

@app.on_message(filters.new_chat_photo)
async def caesarphoto(client, message):
    chat_id = message.chat.id
    photo = await client.download_media(message.chat.photo.big_file_id)
    await client.send_photo(chat_id=chat_id, photo=photo, caption=f"↢ المستخدم  :{message.from_user.mention} \n قام بتغيـرر صوره المجمـوعه \n√")
