from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT
from datetime import datetime
from helper_func import get_readable_time

@Bot.on_message(filters.command('followus'))
async def followus(client: Client, message: Message):
    while True:
         reply_markup=InlineKeyboardMarkup(
                        [
                         [
                          InlineKeyboardButton('𝓜𝓸𝓿𝓲𝓮𝓼 𝓖𝓻𝓸𝓾𝓹', url="t.me/+ADvUFRV3nsljNTM1"),
                          InlineKeyboardButton('Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ', url="t.me/MoviezAddaKan")
                       ],[
                          InlineKeyboardButton("Bᴏᴛ Oᴡɴᴇʀ", url="t.me/captblacknight")
                         ]
                        ]
                    )

@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))


@Bot.on_message(filters.private & filters.incoming)
async def useless(_,message: Message):
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)
