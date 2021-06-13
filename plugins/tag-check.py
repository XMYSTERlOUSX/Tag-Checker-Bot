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

async def flt_admin(_, client, message):
    try:
        user = await client.get_chat_member(message.chat.id, message.from_user.id)
        return True if user.status in ["administrator", "creator"] else False
    except Exception:
        pass    

admin = filters.create(flt_admin)

@Client.on_message(~anonymous & ~admin & filters.group)
async def addorno(client, message):
    firs = message.from_user.first_name
    las = message.from_user.last_name
    channel = Config.Tag_Check_Group
    chat_id = message.chat.id
    user_id = message.from_user.id
    REPLY_MARKUP = InlineKeyboardMarkup([
    [InlineKeyboardButton("Unmute Me ⚠️",
                          callback_data=f"unmute_{user_id}")]])
    if Config.Tag_Name in firs:
        a=1
    elif las is not None:
        if Config.Tag_Name in las:
            a=1
        else:
            a=0
    elif user_id == 1023936257:
        a=1
    else:
        a=0
    if a == 0:
        try:
            await client.restrict_chat_member(
                channel, user_id, ChatPermissions(can_send_messages=True)
            )
        except BaseException as be:
            await message.reply_text(text=f"""I think I don't have perimission of restricting members in this chat! So I couldn't mute {message.from_user.mention} here!🤷‍♀ Please give me all permissions!""")
            return
        await message.reply_text(text=f"""{message.from_user.mention} you have been muted because you have <b>not added</b> our group tag in your name!
        
If you want to <b>get unmuted</b> please follow the instructions below!👇:-

1. Put `{Config.Tag_Name}`(Tap to copy) in your name.
2. After setting the tag press the below <b>Unmute Me ⚠️</b> button!

If you do all the things correctly you will get unmuted instantly!""",
                                quote=True,
                                reply_markup=REPLY_MARKUP)
                                       
@Client.on_callback_query(filters.regex("unmute_(.*)"))
async def unmute(client, cb):
    chat_id = cb.chat.id
    user_id = cb.from_user.id
    channel = Config.Tag_Check_Group
    firs = cb.from_user.first_name
    las = cb.from_user.last_name
    if Config.Tag_Name in firs:
        b=1
    elif las is not None:
        if Config.Tag_Name in las:
            b=1
        else:
            b=0
    else:
        b=0
    user = cb.matches[0].group(1)
    if cb.from_user.id != user:
        await cb.answer("This Button is not for you⚠️ Please do not press this again! You haven't even been unmuted so you can already talk freely!", show_alert=True)
        return
    if b == 1:
        try:
            await client.restrict_chat_member(
                channel, user, ChatPermissions(can_send_messages=True)
            )
            await cb.answer("You have unmuted yourself successfully!")
            await message.delete()
            await client.send_message(
            chat_id=Config.Log_Group_id,
            text=f"""👇 Below user is unmuted successfully-
<b>User</b> - {cb.from_user.mention}
<b>User First Name</b> - {cb.from_user.first_name}
<b>User Last Name</b> - {cb.from_user.last_name}
<b>User id</b> - `{cb.from_user.id}`"""
)
        except Exception:
            pass
    else:
        await cb.answer("You have still not added our group tag in your name!😡", show_alert=True)
        
        
        
        
        
        
