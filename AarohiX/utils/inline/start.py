from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AarohiX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
                [
                    InlineKeyboardButton(
                        "★ Add Me ★", url=f"https://t.me/Shalinixmusicbot?startgroup=true")
                ],
                [
                     InlineKeyboardButton(
                        "ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="settings_back_helper")
                ],
                [
                    InlineKeyboardButton(
                        "ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/ShaliniMusicBotSh"),
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/music_world_sh"),
                ],    
                [
                     InlineKeyboardButton(
                      "💞ᴍᴀɪɴᴛᴀɪɴᴇʀ💞", url=f"https://t.me/shalini_shalu_69")
                ]
    ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
                [
                    InlineKeyboardButton(
                        "★ Add Me ★", url=f"https://t.me/Shalinixmusicbot?startgroup=true")
                ],
                [
                     InlineKeyboardButton(
                        "ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="settings_back_helper")
                ],
                [
                    InlineKeyboardButton(
                        "ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/ShaliniMusicBotSh"),
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/music_world_sh"),
                ],    
                [
                     InlineKeyboardButton(
                      "💞ᴍᴀɪɴᴛᴀɪɴᴇʀ💞", url=f"https://t.me/shalini_shalu_69")
                ]
    ]
    return buttons
