import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config(object):
    BOT_TOKEN = os.getenv("BOT_TOKEN")  # from @botfather
    API_ID = int(os.getenv("API_ID"))  # from https://my.telegram.org/apps
    API_HASH = os.getenv("API_HASH")  # from https://my.telegram.org/apps
    Tag_Name = os.getenv("Tag_Name", None) # The Tag name you want to set for checking
    Bot_url = os.getenv("Bot_url", None) # The bot's telegram link. Ex:-https://t.me/your_bot?start=start Note:- Include "?start=start" at the end of the url!
    Group1_name = os.getenv("Group1_name", None)
    Group2_name = os.getenv("Group2_name", None)
    Group3_name = os.getenv("Group3_name", None)
    unmute_command_1 = os.getenv("unmute_command_1", None)
    unmute_command_2 = os.getenv("unmute_command_2", None)
    unmute_command_3 = os.getenv("unmute_command_3", None)
    Group1_id = os.getenv("Group1_id", None)
    Group2_id = os.getenv("Group2_id", None)
    Group3_id = os.getenv("Group3_id", None)
    Log_Group = os.getenv("Log_Group", None)
    START_MSG = os.getenv("START_MSG", None)

    
