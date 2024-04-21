import asyncio
from pyrogram import Client, filters
from AarohiX.utils.decorators import AdminRightsCheck
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AarohiX.misc import SUDOERS
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram,YouTube, app)
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
                        
@app.on_message(filters.command("^/start"), group=39)
async def cpanel(_, message: Message):
    if message.from_user.id in SUDOERS:
       await message.reply_text(
                "اهلا عزيزي المطور\nاليك لوحة التحكم الخاصة بالبوت",
                reply_markup=ReplyKeyboardMarkup(
                    [
                        ["تفعيل التواصل", "/broadcast", "حالة التواصل"],
                        ["ضع قناة الاشتراك", "حذف قناة الاشتراك"],
                        ["اذاعة للمطورين", "اذاعة للأساسيين", "اذاعة للقنوات"],
                        ["اذاعة للكل",],
                        ["الاوامر","الاحصائيات"],
                        ["حذف حساب مساعد","اضف حساب مساعد"],
                        ["المحظورين عام","مطور البوت"],
                    ],
                    resize_keyboard=True
                )
            )
    else:
       await message.reply_text(
                "اهلا عزيزي العضو\nاليك لوحة التحكم الخاصة بالبوت",
                reply_markup=ReplyKeyboardMarkup(
                    [
                        ["مطور البوت", "مبرمج السورس"],
                        ["السورس","اصدار"],
                        ["اقتباس","استوري"],
                        ["انمي","متحركه"],
                        ["تويت", "صراحه"],
                        ["نكته","احكام"],
                        [" لو خيروك","انصحني"],
                        ["قران","نقشبندي"],
                        ["اذكار","كتابات"],
                        ["حروف","بوت"],
                        ["غنيلي","سوال"],
                        ["تلاوات","عبدالباسط"],
                        ["افاتار بنات","افاتار شباب"],
                        ["❎ ¦ حذف الكيبورد"]      
                    ],
                    resize_keyboard=True
                )
            )     

