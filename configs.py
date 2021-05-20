import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config(object):
    BOT_TOKEN = os.getenv("BOT_TOKEN")  # from @botfather
    API_ID = int(os.getenv("API_ID"))  # from https://my.telegram.org/apps
    API_HASH = os.getenv("API_HASH")  # from https://my.telegram.org/apps
    Tag_Name = os.getenv("Tag_Name", None) # The Tag name you want to set for checking
    Bot_url = os.getenv("Bot_url", None) # The bot's telegram link. Ex:-https://t.me/your_bot?start=start  Note:- Include "?start=start" at the end of the url!
    Group1_name = os.getenv("Group1_name", None) # Your First Group's name where you want to check user's tags.
    Group2_name = os.getenv("Group2_name", None) # Your Second Group's name where you want to check user's tags.
    Group3_name = os.getenv("Group3_name", None) # Your Third Group's name where you want to check user's tags.
    unmute_command_1 = os.getenv("unmute_command_1", None) # A command name to unmute users who has been muted in the first group. (write the name without the '/' symbol)
    unmute_command_2 = os.getenv("unmute_command_2", None) # A command name to unmute users who has been muted in the second group. (write the name without the '/' symbol)
    unmute_command_3 = os.getenv("unmute_command_3", None) # A command name to unmute users who has been muted in the third group. (write the name without the '/' symbol)
    Group1_id = os.getenv("Group1_id", None) # Your First Group's id where you want to check user's tags.(must include -100 in front)
    Group2_id = os.getenv("Group2_id", None) # Your Second Group's id where you want to check user's tags.(must include -100 in front)
    Group3_id = os.getenv("Group3_id", None) # Your Third Group's id where you want to check user's tags.(must include -100 in front)
    Log_Group_id = os.getenv("Log_Group_id", None) #Make a log group to save the details of who has been unmuted. Input the group id here.(must include -100 in front)
    START_MSG = os.getenv("START_MSG", None) # Enter the message you want to get displayed when users press /start

    
