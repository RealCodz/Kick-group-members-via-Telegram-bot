from telethon import TelegramClient
from telethon.tl.types import ChannelParticipantsAdmins

# 🚀 |  T.me/RealCodz  👤  |  T.me/xqxxqqxq ✈️
# ستخرج ايبي وا ايبي هاش عبر 
# https://my.telegram.org/auth

api = 27244343  # ايدي الايبي 
h = "79588b8147992b9afebec1695b78b1d0"  # هاش الايبي 
tok = ""  # توكن البوت 
userg = "@"  # يوزر الكروب 

bot = TelegramClient("bot", api, h).start(bot_token=tok)

async def k():
    a = []
    
    async for u in bot.iter_participants(userg, filter=ChannelParticipantsAdmins):
        a.append(u.id)
    
    async for u in bot.iter_participants(userg):
        if u.id not in a:
            try:
                await bot.kick_participant(userg, u)
            except:
                pass

with bot:
    bot.loop.run_until_complete(k())