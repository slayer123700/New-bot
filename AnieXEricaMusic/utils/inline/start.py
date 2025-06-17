

from pyrogram.types import InlineKeyboardButton
import config
from AnieXEricaMusic import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇs", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ɪɴ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="ᴜᴛɪʟɪᴛʏ ᴄᴏᴍᴍᴀɴᴅs", callback_data="settings_back_helper"),
        ]
    ]
    return buttons
