import logging
from pyrogram import Client
from configs import Config

logging.basicConfig(level=logging.INFO)

TagcheckerBot = Client('Tag checker',
                  api_id=Config.API_ID,
                  api_hash=Config.API_HASH,
                  bot_token=Config.BOT_TOKEN,
                  plugins=dict(root="plugins"))

TagcheckerBot.run()
