# (c) Asm Safone
# A Part of MegaDL-Bot <https://github.com/AsmSafone/MegaDL-Bot>


import os

class Config:
    API_ID = int(os.environ.get("API_ID", 123))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    TG_MAX_SIZE = 2040108421
    OWNER_ID = int(os.environ.get("OWNER_ID", 1316963576))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    LOG_CHANNEL_UNAME = os.environ.get("LOG_CHANNEL_UNAME", "")


class TEXT:
  ABOUT = """
🤖 **Name:** {bot_name}

📝 **Language:** [Python](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted On:** [Heroku](https://heroku.com)

🧑‍💻 **Maintainer:** {bot_owner}

👥 **Support Group:** [IMΛGΣЯ](https://t.me/ImagerSupportGroup)
"""

  HELP_USER = """
This is **{bot_name}**

This Bot Can Download Files & Videos From Mega Links & Upload To Telegram. Just Send Any Mega.nz Link & See The Magic. You Can Also Add or Change Caption: Just Select An Uploaded File/ Video or Forward Me Any Telegram File & Then Write The Text You Want To Be Caption On The File As A Reply To That File & The Text You Wrote Will Be Attached As Caption 😁! 
"""

  START_TEXT = """
👋🏻 **Hi** {user_mention},

I'm **{bot_name}**
I Can Download Files & Videos From Mega.nz Links & Upload To Telegram. Please Check Help To Learn More 😉!

**Maintained By: {bot_owner}**❤️!
"""
