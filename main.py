import logging
from pyrogram import Client
from configs import Config

logging.basicConfig(level=logging.INFO)

AnonyBot = Client('Tag checker',
                  api_id=var.API_ID,
                  api_hash=var.API_HASH,
                  bot_token=var.BOT_TOKEN,
                  plugins=dict(root="plugins"))

AnonyBot.run()
