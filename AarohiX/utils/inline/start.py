from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AarohiX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="👁️‍🗨️➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ➕ 👁️‍🗨️",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="👁️‍🗨️ʜᴇʟᴩ👁️‍🗨️",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="❤‍🔥sᴇᴛᴛɪɴɢs❤‍🔥", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💖 𝗠𝘂𝘀𝗶𝗰 𝗟𝗼𝘃𝗲𝗿𝘀  💖", url=f"https://t.me/music_world_sh"),
            InlineKeyboardButton(
                text="ᴍʏ ʙᴇꜱᴛ 💖", url=f"https://t.me/Bhoomika_Bhumika"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💝𝚘𝚠𝚗𝚎𝚛💝", user_id=OWNER),
            InlineKeyboardButton(
                text="🥰sᴜᴩᴩᴏʀᴛ🥰", url=config.SUPPORT_GROUP
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="👁️‍🗨️➕ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ➕ 👁️‍🗨️",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥺ʜᴇʟᴩ🥺", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💖 𝗠𝘂𝘀𝗶𝗰 𝗟𝗼𝘃𝗲𝗿𝘀 💖", url=f"https://t.me/music_world_sh"),
            InlineKeyboardButton(
                text="🥰 ᴍʏ ʙᴇꜱᴛ 🥰", url=f"https://t.me/Bhoomika_Bhumika"
            ),
        ],
        [
            InlineKeyboardButton(text="💝𝚘𝚠𝚗𝚎𝚛💝", user_id=OWNER),
            InlineKeyboardButton(
                text="🥰sᴜᴩᴩᴏʀᴛ🥰", url=config.SUPPORT_GROUP
            ),
        ],
        [
            InlineKeyboardButton(
                    text="👁️‍🗨️𝚁𝚎𝚙𝚘👁️‍🗨️", url=f"https://telegra.ph/file/440427330b7871341f2cf.mp4"
                )
        ],
     ]
    return buttons
