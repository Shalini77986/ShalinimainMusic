from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AarohiX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🔆ʜᴇʟᴩ🔆",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="❤‍🔥sᴇᴛᴛɪɴɢs❤‍🔥", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="♻️ Mᴜsɪᴄ Wᴏʀʟᴅ ♻️", url=f"https://t.me/MUSIC_WORLD_SH"),
            InlineKeyboardButton(
                text="🌐ᴜᴘᴅᴀᴛᴇs🌐", url=f"https://t.me/ShaliniMusicBotSh"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💞ᴍᴀɪɴᴛᴀɪɴᴇʀ💞", user_id=OWNER),
            InlineKeyboardButton(
                text="✨sᴜᴩᴩᴏʀᴛ✨", url=config.SUPPORT_GROUP
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✨ʜᴇʟᴩ✨", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="♻️ Mᴜsɪᴄ Wᴏʀʟᴅ ♻️", url=f"https://t.me/MUSIC_WORLD_SH"),
            InlineKeyboardButton(
                text="🌐ᴜᴘᴅᴀᴛᴇs🌐", url=f"https://t.me/ShaliniMusicBotSh"
            ),
        ],
        [
            InlineKeyboardButton(text="💞ᴍᴀɪɴᴛᴀɪɴᴇʀ💞", user_id=OWNER),
            InlineKeyboardButton(
                text="🔸sᴜᴩᴩᴏʀᴛ🔹", url=config.SUPPORT_GROUP
            ),
        ],
        [
            InlineKeyboardButton(
                    text="🔎 ᴏᴡɴᴇʀ 🔍", url=f"https://t.me/Heart_heker_69"
                )
        ],
     ]
    return buttons
