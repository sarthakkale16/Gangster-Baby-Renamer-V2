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
	await message.reply_text(f"ғᴀɴᴅᴏᴍ :- <a href='https://t.me/rb1bots'>➪ 𝗥𝘂𝗯𝘆</a>\n➪ ᴄʀᴇᴀᴛᴏʀ :- <a href='https://t.me/sarthakkale16'>✰ʀᴇǫᴜᴇsᴛʙᴏx1✰</a>\n➪ Language :- Python3\n➪ Library :- Pyrogram 2.0\n➪ Server :- KOYEB\n➪ Total Renamed File :- {total_rename}\n➪ Total Size Renamed :- {humanbytes(int(total_size))} \n\n✭ Thank you **<a href='https://t.me/sarthakkale16'>✰ʀᴇǫᴜᴇsᴛʙᴏx1✰</a>** for your hard work \n\n✘ We love you <a href='https://t.me/rb1bots'>**ʀʙ1 ʙᴏᴛs**</a> ❥",quote=True)
