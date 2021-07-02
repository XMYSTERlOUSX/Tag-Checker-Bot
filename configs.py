import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config(object):
    BOT_TOKEN = os.getenv("BOT_TOKEN")  # from @botfather
    API_ID = int(os.getenv("API_ID"))  # from https://my.telegram.org/apps
    API_HASH = os.getenv("API_HASH")  # from https://my.telegram.org/apps
    Tag_Check_Group = os.getenv("Tag_Check_Group", None) # Your Group id where you want to check user's tags.(must include -100 in front)
    Tag_Name = os.getenv("Tag_Name", None) # The Tag name you want to set for checking
    Log_Group_id = os.getenv("Log_Group_id", None) #Make a log group to save the details of who has been unmuted. Input the group id here.(must include -100 in front)
    Bot_url = os.getenv("Bot_url", None) # The bot's telegram link. Ex:-https://t.me/your_bot?start=start  Note:- Include "?start=start" at the end of the url!


    
