import pyrogram
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup
from AarohiX.misc import SUDOERS
from AarohiX import app

admin_keyboard = ReplyKeyboardMarkup([
    ['تحديث السورس 📥'],
    ['رستر البوت 🕹️'],
    ['اذاعه للكل 🔊'],
    ['.'],
    ['.'],
    ['.']
], resize_keyboard=True)

# دالة للتعامل مع أمر /admin
@app.on_message(filters.command("Dev") &  filters.private & SUDOERS)
async def admin(client, message):
    await message.reply("↢ لوحة المفاتيح الخاصة بالمطور", reply_markup=admin_keyboard)

# دالة للتعامل مع الأوامر الأخرى
@app.on_message(filters.text & ~filters.command("Dev") & filters.private & SUDOERS)
async def handle_commands(client, message):
    # أدخل الكود الخاص بمعالجة الأوامر الأخرى هنا
    pass
