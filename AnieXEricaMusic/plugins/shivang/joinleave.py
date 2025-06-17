from pyrogram import Client, filters
from pyrogram.types import Message, ChatMember
import logging
from AnieXEricaMusic import app

logging.basicConfig(level=logging.INFO)

@app.on_message(filters.video_chat_started)
async def video_chat_started(client, message: Message):
    chat = message.chat
    await message.reply(
        f"Vᴏɪᴄᴇ Cʜᴀᴛ ʜᴀs Sᴛᴀʀᴛ Jᴏɪɴ ᴛʜᴇᴍ ᴡʜɪʟᴇ Mᴀɴsʀɪʙᴀᴛɪɴɢ 🥵👻"
    )

@app.on_message(filters.video_chat_ended)
async def video_chat_ended(client, message: Message):
    chat = message.chat
    await message.reply(
        f"Vᴏɪᴄᴇ Cʜᴀᴛ ʜᴀs Eɴᴅᴇᴅ Eᴠᴇʀʏᴏɴᴇ Gᴏɴᴇ ᴛᴏ MᴀɴsʀɪʙᴀTE 🥵👻"
    )
