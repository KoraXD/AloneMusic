from pyrogram import Client
from Alone.tgcalls import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User
from Alone.config import (
    BOT_USERNAME,
)

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hey, I'm Alone Robot VC Assistant, No Message Here Message To @ItzAloneX")
  return