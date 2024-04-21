import os
import requests
import aiohttp
import aiofiles

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton

from AarohiX import app
from AarohiX.plugins.play.filters import command

@app.on_message(command(["تيك"]))
async def tiktok_video(client, message):
    query = " ".join(message.command[1:])
    m = await message.reply_text("<b>↢ جاري تنزيل المقطع الخاص بك 🕜</b>")
    idd = message.from_user.id
    mc = message.chat.id
    url = "https://www.tikwm.com/api/?url={}".format(query)
    res = requests.get(url).json()
    video = res['data']['play']
    title = res['data']['title']
    share = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("• شارك •", url='https://t.me/share/url?url={}'.format(query))
        ]
    ])
    await message.reply_video(
        video=video,
        caption='- {} .'.format(title),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• مشاركه •", url='https://t.me/share/url?url={}'.format(query))
                ],
            ]
        ),
    )
 
