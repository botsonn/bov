from pyrogram import Client, filters, idle
from pyrogram.enums import ChatMemberStatus
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from AarohiX import app
from config import *


mutes = []
@app.on_message(filters.command(["كتم"],"") & filters.group)
async def mute(app,message):
   member = await message.chat.get_member(message.from_user.id)
   if not member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     return await message.reply("↢ ابشر...متأكد انك مشرف ؟")
   else:
     if not message.reply_to_message:
       return await message.reply("↢ قم بعمل ريبلي علي الشخص او شخص ليس مشرفاً\n√")
     member = await message.chat.get_member(message.reply_to_message.from_user.id)
     if member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       return await message.reply("↢ ولك اعذرني انا لا احب ان اكتم مشرفين\n√")
     chat_id = str(message.chat.id)
     user_id = str(message.reply_to_message.from_user.id)
     x = "{}@{}".format(chat_id,user_id)
     if x in mutes:
       return await message.reply("↢ تم كتم هذا الشخص بنجاح \n√")
     else:
       mutes.append(x)
     return   await message.reply_video(
        video = "https://telegra.ph/file/90522f3b21b80c4afdaf6.mp4",
        caption = "↢ المستخدم ⦗ {} ⦘\n\n↢ تم كتمه بواسطه ⦗ {} ⦘ \n√".format(message.reply_to_message.from_user.mention,message.from_user.mention))
              
@app.on_message(filters.command(["الغاء الكتم"],"") & filters.group)
async def unmute(app,message):
   member = await message.chat.get_member(message.from_user.id)
   if not member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     return await message.reply("↢ ابشر...متأكد انك مشرف ؟")
   else:
     if not message.reply_to_message:
       return await message.reply("↢ قم بعمل ريبلي علي الشخص او شخص ليس مشرفاً\n√")
     member = await message.chat.get_member(message.reply_to_message.from_user.id)
     if member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       return await message.reply("↢ ولك اعذرني انا لا احب ان اكتم مشرفين\n√")
     chat_id = str(message.chat.id)
     user_id = str(message.reply_to_message.from_user.id)
     x = "{}@{}".format(chat_id,user_id)
     if not x in mutes:
       return await message.reply("↢ تم الغاء الكتم بنجاح \n√")
     else:
       mutes.remove(x)
       return await message.reply("↢ المستخدم ⦗ {} ⦘ \n\nتم الغاء كتمة بواسطة ⦗ {} ⦘".format(message.reply_to_message.from_user.mention,message.from_user.mention))

@app.on_message(filters.command(["المكتومين"],"")   & filters.group)
def get_dmute(app, message):
   if len(mutes) == 0: return
   member = message.chat.get_member(message.from_user.id)
   if not member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     return message.reply("↢ ابشر...متأكد انك مشرف ؟")
   ch = message.chat.id
   c = 0
   text = "عدد المكتومين في هذه المجـموعه : \n"
   for a in mutes:
     chat_id = int(a.split("@")[0])
     user_id = int(a.split("@")[1])
     if chat_id == ch:
        user = app.get_users(user_id)
        text += f"- {user.mention}\n"
        c += 1
   if c == 0: return message.reply("↢ ابشر جروب لا يوجد به مكتومين")
   message.reply(f"{text}")

@app.on_message(filters.group)
def del_msg(_,m):
   if m.from_user:
     chat_id = str(m.chat.id)
     user_id = str(m.from_user.id)
     x = "{}@{}".format(chat_id,user_id)
   for a in mutes:
     if a == x: 
       m.delete()
       break


app.start()
print("✓✓✓")
idle()
