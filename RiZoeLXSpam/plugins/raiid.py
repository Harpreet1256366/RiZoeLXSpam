
import asyncio
import base64
import os
import random
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import Riz, Riz2, Riz3, Riz4, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, Riz11, Riz12, Riz13, Riz14, Riz15, Riz16, Riz17, Riz18, Riz19, Riz20, RAID, RRAID, SUDO_USERS

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

que = {}
RiZoeLX = [1517994352, 2086101519]





@Riz.on(events.NewMessage(pattern=r"\.quiz"))
@Riz2.on(events.NewMessage(pattern=r"\.quiz"))
@Riz3.on(events.NewMessage(pattern=r"\.quiz"))
@Riz4.on(events.NewMessage(pattern=r"\.quiz"))
@Riz5.on(events.NewMessage(pattern=r"\.quiz"))
@Riz6.on(events.NewMessage(pattern=r"\.quiz"))
@Riz7.on(events.NewMessage(pattern=r"\.quiz"))
@Riz8.on(events.NewMessage(pattern=r"\.quiz"))
@Riz9.on(events.NewMessage(pattern=r"\.quiz"))
@Riz10.on(events.NewMessage(pattern=r"\.quiz"))
@Riz11.on(events.NewMessage(pattern=r"\.quiz"))
@Riz12.on(events.NewMessage(pattern=r"\.quiz"))
@Riz13.on(events.NewMessage(pattern=r"\.quiz"))
@Riz14.on(events.NewMessage(pattern=r"\.quiz"))
@Riz15.on(events.NewMessage(pattern=r"\.quiz"))
@Riz16.on(events.NewMessage(pattern=r"\.quiz"))
@Riz17.on(events.NewMessage(pattern=r"\.quiz"))
@Riz18.on(events.NewMessage(pattern=r"\.quiz"))
@Riz19.on(events.NewMessage(pattern=r"\.quiz"))
@Riz20.on(events.NewMessage(pattern=r"\.quiz"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        RiZoeL = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(RiZoeL) == 2:
            user = str(RiZoeL[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in RiZoeLX:
                text = f"I can't raid on @RiZoeLX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SMEX_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(RiZoeL[0])
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.5)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in RiZoeLX:
                text = f"I can't raid on @RiZoeLX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SMEX_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = b.first_name
                counter = int(RiZoeL[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)




@Riz.on(events.NewMessage(pattern=r"\.dquiz"))
@Riz2.on(events.NewMessage(pattern=r"\.dquiz"))
@Riz3.on(events.NewMessage(pattern=r"\.dquiz"))
@Riz4.on(events.NewMessage(pattern=r"\.dquiz"))
@Riz5.on(events.NewMessage(pattern=r"\.dquiz"))
@Riz6.on(events.NewMessage(pattern=r"\.dquiz"))
@Riz7.on(events.NewMessage(pattern=r"\.dquiz"))
@Riz8.on(events.NewMessage(pattern=r"\.dquiz"))
@Riz9.on(events.NewMessage(pattern=r"\.dquiz"))
@Riz10.on(events.NewMessage(pattern=r"\.dquiz"))
@Riz11.on(events.NewMessage(pattern=r"\.dquiz"))
@Riz12.on(events.NewMessage(pattern=r"\.dquiz"))
@Riz13.on(events.NewMessage(pattern=r"\.dquiz"))
@Riz14.on(events.NewMessage(pattern=r"\.dquiz"))
@Riz15.on(events.NewMessage(pattern=r"\.dquiz"))
@Riz16.on(events.NewMessage(pattern=r"\.dquiz"))
@Riz17.on(events.NewMessage(pattern=r"\.dquiz"))
@Riz18.on(events.NewMessage(pattern=r"\.dquiz"))
@Riz19.on(events.NewMessage(pattern=r"\.dquiz"))
@Riz20.on(events.NewMessage(pattern=r"\.dquiz"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    global que    
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(Rizoel[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Quiz"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Quiz"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
