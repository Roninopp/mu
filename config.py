## What's up Kangers
## Thanks Team Zaid 'Arigatou'

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
if str(getenv("SESSION_NAME")).strip() == "":
    SESSION_NAME = str(None)
else:
    SESSION_NAME = str(getenv("SESSION_NAME"))

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "Umk")

API_ID = int(getenv("API_ID", "7311387"))
API_HASH = getenv("API_HASH", "77449cfdebb052e2f512e69223956e52")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Cloner:Cloner@cluster0.cgc6t.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Ronin tm")
OWNER_USERNAME = getenv("OWNER_USERNAME", "DushmanXRonin")
ALIVE_NAME = getenv("ALIVE_NAME", "Fantastic")
BOT_USERNAME = getenv("BOT_USERNAME", "FANTASTICFIGHTERBOT")
OWNER_ID = getenv("OWNER_ID", "1978498226")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Fantastic Music Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Ronin_Fighters_Fd")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "RoninXJin_updates")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1793699293").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/9012a958e07362727ae19.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/9012a958e07362727ae19.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Roninopp/mu")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph//file/6553e1b6bab59d5aefb82.jpg")
QUE_IMG = getenv("QUE_IMG", "https://te.legra.ph/file/9012a958e07362727ae19.jpg")
CMD_IMG = getenv("CMD_IMG", "https://te.legra.ph/file/9012a958e07362727ae19.jpg")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph//file/1cc56612349e180fcd25a.jpg")
SKIP_IMG = getenv("SKIP_IMG", "https://te.legra.ph/file/9012a958e07362727ae19.jpg")
NEXT_IMG = getenv("NEXT_IMG", "https://te.legra.ph/file/9012a958e07362727ae19.jpg")
HEROKU_MODE = getenv("HEROKU_MODE", None)
