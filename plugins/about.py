import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"➪ ᴍᴀɴᴀɢᴇᴅ ʙʏ :- <a href='https://t.me/rb1bots'> ʀʙ1 ʙᴏᴛs</a>\n➪ ᴄʀᴇᴀᴛᴏʀ :- <a href='https://t.me/sarthakkale16'>✰ ʀᴇǫᴜᴇsᴛʙᴏx1 ✰</a>\n➪ ʟᴀɴɢᴜᴀɢᴇ :- ᴘʏᴛʜᴏɴ 3\n➪ ʟɪʙʀᴀʀʏ:- ᴘʏʀᴏɢʀᴀᴍ 2.0\n➪ ᴅᴇᴠ : @know_sarthak16\n➪ ᴛᴏᴛᴀʟ ғɪʟᴇ ʀᴇɴᴀᴍᴇs :- {total_rename}\n➪ ᴛᴏᴛᴀʟ sɪᴢᴇ ʀᴇɴᴀᴍᴇᴅ:- {humanbytes(int(total_size))} \n\n✭ ᴛʜᴀɴᴋ ʏᴏᴜ **<a href='https://t.me/sarthakkale16'>✰ ʀᴇǫᴜᴇsᴛʙᴏx1 ғᴀᴍɪʟʏ ✰</a>** \nғᴏʀ ʏᴏᴜʀ sᴜᴘᴘᴏʀᴛ\n✘ ᴡᴇ ʟᴏᴠᴇ ʏᴏᴜ ᴀɴᴅ sᴛᴀɴᴅ ʙʏ ʏᴏᴜ <a href='https://t.me/rb1bots'>**ʀʙ1 ʙᴏᴛs**</a> ❥",quote=True)
