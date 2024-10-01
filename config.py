import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7463305761:AAEm0Hw0-HUKmQRRxdG53YM7U6sKVo7rJ2I")
APP_ID = int(os.environ.get("APP_ID", "21145186"))
API_HASH = os.environ.get("API_HASH", "daa53f4216112ad22b8a8f6299936a46")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002465123057"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6011680723"))
PORT = os.environ.get("PORT", "8074")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://infohubstore06:CUXzlOmJvWITtrxn@gamingthree.i5ogs.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "gamingthree")

#Shortner (token system) 

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "hypershort.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "28cb820c966371de4aff06fc22d6a8a0bcf62b2c")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/infohub_updates/34") 

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002123546604"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002398866124"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1002263475051"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/WhV.jpg")

#start message
START_MSG = os.environ.get("START_MESSAGE", "ʜᴇʟʟᴏ ᴛʜᴇʀᴇ {mention}!!🌚\n\nɪ ꜱʜᴀʀᴇ ꜰɪʟᴇꜱ ᴡɪᴛʜɪɴ ɪɴꜰᴏʜᴜʙ ɴᴇᴛᴡᴏʀᴋꜱ ᴀɴᴅ ʏᴏᴜ ᴀʀᴇ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴜꜱᴇ ᴍᴇ! ⚡️")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5178714818").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ ᴛʜᴇʀᴇ {mention}!!👋\n\n<b>ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴇꜱ, ʏᴏᴜ ᴀʀᴇ ʀᴇQᴜᴇꜱᴛᴇᴅ ᴛᴏ ꜱᴜᴘᴘᴏʀᴛ ᴜꜱ ʙʏ ᴊᴏɪɴɪɴɢ ᴛʜᴇ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ɢʀᴏᴜᴘꜱ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ:</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @book_novel_pdfs_audiobooks_free</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ꜱᴏʀʀʏ ʙᴜᴛ ᴏɴʟʏ ᴀᴜᴛʜᴏʀɪꜱᴇᴅ ᴀᴅᴍɪɴꜱ ꜰʀᴏᴍ <b>ɪɴꜰᴏʜᴜʙ ɴᴇᴛᴡᴏʀᴋꜱ</b> ᴄᴀɴ ᴜꜱᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ. ᴛᴏ ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴀᴅᴍɪɴꜱ, ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍʏ ꜰʀɪᴇɴᴅ - @infohubsupport_robot"

ADMINS.append(OWNER_ID)
ADMINS.append(6011680723)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
