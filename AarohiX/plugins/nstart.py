import asyncio
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
import config
from config import BANNED_USERS
from config import OWNER_ID
from AarohiX import app
from strings import get_string
from AarohiX.utils.inline import start_pannel
from AarohiX.utils.decorators.language import LanguageStart

@app.on_message(
    filters.command("start"))
   


@LanguageStart
async def str(client, message: Message, _):    
    await message.reply_sticker("CAACAgUAAxkBAAEK0m5lY2Isl01ccCwHjdWpxMJ-_y2yvwACnwgAAivsiVVkOxHqpEe-GjME")   
    return await message.reply_photo(
               photo=config.START_IMG_URL,
               caption=_["start_2"].format(
            config.MUSIC_BOT_NAME
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★ Add Me ★", url=f"https://t.me/ANNIE_BOT?startgroup=true")
                ]
                
           ]
        ),
)
