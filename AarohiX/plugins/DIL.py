from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from AarohiX import app
import string
from strings import get_command

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

DIL = [" **◈ ━━━━━━━ ⸙ ♡ ⸙ ━━━━━━━ ◈** \n\n🍃**ʀᴇʟᴀᴛɪᴏɴsʜɪᴘ ᴅᴏsᴇɴ'ᴛ ɴᴇᴇᴅ ᴄᴜᴛᴇ ᴠᴏɪᴄᴇ ᴀɴᴅ ʟᴏᴠᴇʟʏ ғᴀᴄᴇ...**🍃 \n\n**ᴍʏ ꜰᴀᴠᴏᴜʀɪᴛᴇ 🧐 ᴘᴇʀꜱᴏɴ ɪɴ ᴡᴏʀʟᴅ ɪꜱ ᴍʏ ʙᴇꜱᴛɪᴇ ʙʜᴏᴏᴍɪᴋᴀ** \n\n**◈ ━━━━━━━ ⸙ ♡ ⸙ ━━━━━━━ ◈** ",
       " **◈ ━━━━━━━ ⸙ ♡ ⸙ ━━━━━━━ ◈** \n\n🍃**🌹❝◂ Ek Ladke Ne Ek Ladki Ko Kamal Ka Phul Diya Ladki Ne Usko Ek Thappad Mar Diya ▸**🍃 \n\n**◂Ladka Bola Me To BJP Ka Parchar Kar Raha Hu Ladki Boli Me Bhi Congress Ka Parchar Kar Rahi Hu🤣.❞🌹** \n\n**◈ ━━━━━━━ ⸙ ♡ ⸙ ━━━━━━━ ◈** ",
       " **◈ ━━━━━━━ ⸙ ♡ ⸙ ━━━━━━━ ◈** \n\n 🍃**Koyi Aaye Na Jaye Na, Aao Na Aisi Jagah Pe Le Chalun**🍃 \n\n**✨❤️ Jahaan Waqt Humara Ruka Ho,Aur Main Apne Dil Ki Kahun ♥️✨** \n\n**◈ ━━━━━━━ ⸙ ♡ ⸙ ━━━━━━━ ◈** "]

# Command of DILxAAROHI
DIL_COMMAND = get_command("DIL_COMMAND")

@app.on_message(
    filters.command(DIL_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(DIL),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎶𝕄𝕦𝕤𝕚𝕔 𝕎𝕠𝕣𝕝𝕕🎶", url=f"https://t.me/music_world_sh"),
                    InlineKeyboardButton(
                        "💝ᴍᴀɪɴᴛᴀɪɴᴇʀ💝", url=f"https://t.me/Shalini_shalu_69")
                    
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(DIL_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(DIL),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎶𝕄𝕦𝕤𝕚𝕔 𝕎𝕠𝕣𝕝𝕕🎶", url=f"https://t.me/music_world_sh"),
                    InlineKeyboardButton(
                        "💝ᴍᴀɪɴᴛᴀɪɴᴇʀ💝", url=f"https://t.me/Shalini_shalu_69")
                    
                ]
            ]
        ),
    )
