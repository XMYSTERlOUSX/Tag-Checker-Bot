import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config(object):
    BOT_TOKEN = os.getenv("BOT_TOKEN")  # from @botfather
    API_ID = int(os.getenv("API_ID"))  # from https://my.telegram.org/apps
    API_HASH = os.getenv("API_HASH")  # from https://my.telegram.org/apps
    Tag_Check_Group = os.getenv("Tag_Check_Group", None) #the group id where you want to chech user's tags

    