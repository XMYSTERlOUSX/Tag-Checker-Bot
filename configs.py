import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config(object):
    BOT_TOKEN = os.getenv("BOT_TOKEN")  # from @botfather
    API_ID = int(os.getenv("API_ID"))  # from https://my.telegram.org/apps
    API_HASH = os.getenv("API_HASH")  # from https://my.telegram.org/apps
    Allowed_USERS = os.getenv("Allowed_USERS").split() # Allowed user's ids to be without the tag except admins.(seperate ids with space)
    Tag_Check_Group = os.getenv("Tag_Check_Group", None) # Your Group id where you want to check user's tags(with -100 in front)
    Tag_Name = os.getenv("Tag_Name", None) # The Tag name you want to set for checking
    Bot_url = os.getenv("Bot_url", None) # The bot's telegram link

    
