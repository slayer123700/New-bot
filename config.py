
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "22250152"))
API_HASH = getenv("API_HASH", "d071b95a90a941c3d2af8a27e3e52d12")
BOT_PRIVACY = getenv("BOT_PRIVACY", "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
BOT_TOKEN = getenv("BOT_TOKEN", "7979900579:AAFQBE54bCFSvLH2s8XLBG9qvflGD85Ol2A")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://musicbotxd:musicbotxd@cluster0.6thyk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

DEEP_API = getenv("9e34227f-73df-4f6d-ac59-20a48904b1db") #optional

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID",-1002392274240))

BOT_USERNAME = getenv("BOT_USERNAME", "Shigaraki_probot")
BOT_NAME = getenv("BOT_NAME", "sʜɪɢᴀʀᴀkɪ ᴛᴏᴍᴜʀᴀ")

LOG_GROUP = getenv("LOG_GROUP",-1002392274240)

APPROVAL_GROUP = int(getenv("APPROVAL_GROUP",-1002392274240))

OWNER_ID = int(getenv("OWNER_ID", 6018803920))

OWNER = int(getenv("OWNER", 6018803920))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY","HK543fklqxgt66hvxf")

DEEP_API = getenv("9e34227f-73df-4f6d-ac59-20a48904b1db") #optional 

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/riteshxcoder/New-bot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/MBT_SLAYER")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/+jsCexG6NFnE1YTY1")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

STRING1 = getenv("STRING_SESSION","AQFy0zIAeTrqXAyN24IN6WCSafrxbO81MFls0ObprFIFNDUixJJjgGITAdkghmp2aiWnhMnY-VbLFph-jaMKIEfsw7shXYiB6-qZOVlV0LKm3Imfd8GZ-AWzmj7O_v1VfcwtM8NeLkeJlGbaix6JpQeP_1ZefphDuxdCzrqzEOmaGeWvPj1cs9sjzYgTyAoehubC5XnbVuRU-7Xu6kmPssSQMYMABAZB35EGu47c-RAvyx43MkLKXzBQGKfU2Lx-YElS1U6jCwBTn4z6LYcct7ZT78CT7G-XK-P3PyLylYcGR0j90lGIzud7mJZm8ZNIHc-5NTlG-mxmK3l0MHjNMgW6bM_a9AAAAAGxDHVkAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL =  "https://i.ibb.co/gFg5XstQ/photo-2025-05-24-04-00-24-7507857220025974820.jpg"
PING_IMG_URL = getenv("PING_IMG_URL", "https://i.ibb.co/gFg5XstQ/photo-2025-05-24-04-00-24-7507857220025974820.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/bggrlh.jpg"
STATS_IMG_URL = "https://files.catbox.moe/iffmnv.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/f3yuiy.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/urv7wi.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/6khxhw.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/2tcim5.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/bggrlh.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/iffmnv.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/6khxhw.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/jkqyg2.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
