from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config

@app.on_message(
    command(["مطور السورس", "مبرمج السورس", "تيتو"])
)
async def maker(client: Client, message: Message):
    await message.reply_video(
        video="https://telegra.ph/file/9ccdf1b81efa30d2adb53.mp4",
        caption="• ხ᥆ƚ ძᥱ᥎ᥱᥣ᥆ρᥱᖇ 🇵🇸 \n ━━━━━━━━━━━━ \n • bot ↦ {config.BOT_USER} . ",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ძᥱ᥎ᥣ᥆ρᥱᖇ 🇵🇸", url=f"tg://openmessage?user_id={config.OWNER_ID}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "𝗖𝗛 🇵🇸", url=config.SUPPORT_CHAT
                    ),
                ],
            ]
        ),
    )
