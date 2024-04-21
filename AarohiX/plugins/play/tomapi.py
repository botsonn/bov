import asyncio
import os
from pyrogram.types import CallbackQuery
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(
    filters.command("tnt")
    
)
async def cr_source(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/dcfb16b43f82c3a82c2aa.mp4",
        caption=f"""**مرحبا بك عزيزي {message.from_user.mention}\nانا بوت الذكاء الاصطناعي الخاص بسورس تيتو \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اهـلا بك في سورس تيتو", callback_data="usage"), 
                 ],[
                    InlineKeyboardButton(
                        "，ᥲ ɦ ꪔ ᥱ ძ 𓏺 ¹𖥻", url=f"https://t.me/TOPTETO"),
                    InlineKeyboardButton(
                        "🇦🇱⃝⃤|『 𝗧𝗘𝗧𝗢 』تيـتو . 𖡛“", url=f"https://t.me/G_7_Rr"),
                ],[
                
                    InlineKeyboardButton(
                        "𝗦𝗼𝘂𝗥𝗰𝗲 𝗧𝗲𝘁𝗼", url=f"https://t.me/WX_PM"),
                ],

            ]

        ),

    )

    
@app.on_callback_query(filters.regex("usage"))
async def cr_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**الذكاء الاصتناعي 🥺**
★¦ اهلا بك عزيزي في قسم الأوامر
★¦ لتتمكن من تشغيل الذكاء الاصطناعي فقط اكتب
★¦ /gpt - لـلـسـؤال آي سـؤال بالـذكـاء الاسـطـناعي

**الذكاء الاصتناعي**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ارجع •", callback_data="back"), 
                ]
            ]
        )
    )

    
@app.on_callback_query(filters.regex("back"))
async def cr_back(_, callback_query: CallbackQuery):
    message = callback_query.message
  
    await message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("اهلا بـك في سورس تيتو", callback_data="tommm")],
            [InlineKeyboardButton("，ᥲ ɦ ꪔ ᥱ ძ 𓏺 ¹𖥻", url=f"https://t.me/TOPTETO"),
             InlineKeyboardButton("🇦🇱⃝⃤|『 𝗧𝗘𝗧𝗢 』تيـتو . 𖡛“", url=f"https://t.me/G_7_Rr")],
            [InlineKeyboardButton("𝗦𝗼𝘂𝗥𝗰𝗲 𝗧𝗲𝘁𝗼", url=f"https://t.me/wx_pm")],
        ]
    ))

