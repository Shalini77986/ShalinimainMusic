from pyrogram import filters
from pyrogram.types import Message

from .. import app



@app.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"Hello This is {message.from_user.first_name},\n\n๏ \nTelegram Group Calls Streaming bot with some useful features, written in Python with Pyrogram and Py-Tgcalls. Supporting platforms like Youtube, Spotify, Resso, AppleMusic, Soundcloud and M3u8 Links.",
        
    )
