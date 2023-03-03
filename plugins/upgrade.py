"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🥈 Silver Tier ** 
	Daily  Upload  limit 10GB
	Price Rs 51  ind /🌎 0.7$  per Month
	
	**🪙 Gold Tier 🪙**
	Daily Upload limit 35GB
	Price Rs 101 ind /🌎 1.24$  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 90GB
	Price Rs 201  ind /🌎 2.46$  per Month
	
	
	Pay Using Upi I'd ```chaitu104@ybl```
	
	After Payment Send Screenshots Of 
        Payment To Admin @sarthakkale16"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Admin",url = "https://t.me/sarthakkale16")], 
        			[InlineKeyboardButton("Ask Payment Link",url = "https://t.me/sarthakkale16"),
        			InlineKeyboardButton("Ask Payment Link",url = "https://p.paytm.me/xCTH/vo37hii9")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🥈 Silver Tier ** 
	Daily  Upload  limit 10GB
	Price Rs 51  ind /🌎 0.7$  per Month
	
	**🪙 Gold Tier 🪙**
	Daily Upload limit 35GB
	Price Rs 101 ind /🌎 1.24$  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 90GB
	Price Rs 201  ind /🌎 2.46$  per Month
	
	
	Pay Using Upi I'd ```chaitu104@ybl```
	
	After Payment Send Screenshots Of 
        Payment To Admin @sarthakkale16"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Admin",url = "https://t.me/sarthakkale16")], 
        			[InlineKeyboardButton("Ask Payment Link",url = "https://t.me/sarthakkale16"),
        			InlineKeyboardButton("Ask Payment Link",url = "https://p.paytm.me/xCTH/vo37hii9")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
