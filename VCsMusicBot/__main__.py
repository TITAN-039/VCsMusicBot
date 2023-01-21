import requests
from pyrogram import Client as Bot

from VCsMusicBot.config import API_HASH
from VCsMusicBot.config import API_ID
from VCsMusicBot.config import BG_IMAGE
from VCsMusicBot.config import BOT_TOKEN
from VCsMusicBot.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID, "23785459"
    API_HASH, "4ad74412e0cff337b063c655bd72807d"
    bot_token=BOT_TOKEN, "5731586246:AAFJ9yVZ26B_DU9a5z4BpoqAOkgzGHrU78Q"
    plugins=dict(root="VCsMusicBot.modules"),
)

bot.start()
run()
