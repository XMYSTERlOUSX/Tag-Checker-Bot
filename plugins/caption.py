#All Rights Reserved! @xmysteriousx

from pyrogram import (
    Client,
    filters
)
from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired
)
from pyrogram.types import (
    ChatPermissions,
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from configs import Config

async def anon_filter(_, __, m: Message):
    return bool(m.from_user is None and m.sender_chat)

anonymous = filters.create(anon_filter)
@Client.on_message(~anonymous & filters.group)
async def addorno(client, message):
    firs = message.from_user.first_name
    las = message.from_user.last_name
    chat_id = message.chat.id
    user_id = message.from_user.id
    REPLY_MARKUP = InlineKeyboardMarkup([
    [InlineKeyboardButton("Unmute Me ⚠️",
                          url="https://t.me/tag_check_bot?start=start")]])
    if "⫷[ʘϾḂ]⫸" in firs:
        a=1
    elif las is not None:
        if "⫷[ʘϾḂ]⫸" in las:
            a=1
        else:
            a=0
    elif user_id == 1023936257:
        a=1
    else:
        a=0
    if a == 0:
        await message.reply_text(text=f"""{message.from_user.mention} you have been muted because you have <b>not added</b> our group tag in your name!

If you want to <b>get unmuted</b> please follow the instructions below!👇:-

1. Put `⫷[ʘϾḂ]⫸`(Tap to copy) in your name.
2. After setting the tag press the below <b>Unmute Me ⚠️</b> button and press /start to the bot!

If you do all the things correctly you will get unmuted instantly!""",
                                quote=True,
                                reply_markup=REPLY_MARKUP)
                                
        await client.restrict_chat_member(
            chat_id, user_id, ChatPermissions(can_send_messages=False)
        )
            
@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    channel = Config.Tag_Check_Group
    firs = message.from_user.first_name
    las = message.from_user.last_name
    if "⫷[ʘϾḂ]⫸" in firs:
        b=1
    elif las is not None:
        if "⫷[ʘϾḂ]⫸" in las:
            b=1
        else:
            b=0
    elif user_id == 1023936257:
        b=1
    else:
        b=0
    if b == 1:
        await client.restrict_chat_member(
            channel, user_id, ChatPermissions(can_send_messages=True)
        )
        await message.reply_text(text=f"""{message.from_user.mention}, You have <b>unmuted yourself</b> successfully!\nNow you can chat in our group as much as you want🥳""", reply_to_message_id=chat_id)
    else:
        await message.reply_text(text=f"""Oh come on {message.from_user.mention}! You have still not added our group tag in your name!😡 So you are still muted😝

If you want to <b>get unmuted</b> please follow the instructions below!👇:-

1. Put `⫷[ʘϾḂ]⫸`(Tap to copy) in your name.
2. After setting the tag press /start in the bot!

If you do all the things correctly you will get unmuted instantly!""",  reply_to_message_id=chat_id)
