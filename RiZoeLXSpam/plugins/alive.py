from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version
from time import time
from datetime import datetime

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/1cb0eddf8bbadb3d8d0f4.jpg"
  

          
rizoel = "✧ QUIZ BOT IS ALIVE\n\n"

rizoel += f"┏━━━━━━━━━━━━━━━━━━━\n"

rizoel += f"┣➣ **Made And Managed By @CKD_OWNER** : `3.9.6`\n"

rizoel += f"┣➣ **▪︎Powered By Suzune▪︎**`\n"

rizoel += f"┗━━━━━━━━━━━━━━━━━━━\n\n"
          
                                    
@Riz.on(events.NewMessage(pattern=r"\.alive"))
async def alive(event):
    if event.sender_id in SMEX_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel)
    
