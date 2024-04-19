from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config

#writing by teto @G_7_Rr          
                
@app.on_message(filters.command(["السورس"],""))
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://graph.org/file/862ce6e007a09bfd9d2a8.mp4",
        caption=f"""˛ ╭──── • ◈ • ────╮
么 [𝗦𝗼𝘂𝗿𝗰𝗲 𝗧𝗲𝘁𝗼](https://t.me/t7_au)
么 [𝗔𝗦𝗞 𝗧𝗢 𝗠𝗘](https://t.me/G_7_Rr)
么 [𝗔𝗵𝗺𝗲𝗗 𝗧𝗲𝘁𝗼](https://t.me/TopTeto)
么 [𝗧𝗲𝘁𝗼²](https://t.me/G_7_Rr)
╰──── • ◈ • ────╯
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "AhMeed Teto 🖤", url=f"https://t.me/TopTeto"), 
                 ],[
                   InlineKeyboardButton(
                        "CH SOURCE", url=f"https://t.me/WX_PM"),
                ],

            ]

        ),

    )
    
