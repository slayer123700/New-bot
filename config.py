
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "22250152"))
API_HASH = getenv("API_HASH", "d071b95a90a941c3d2af8a27e3e52d12")
BOT_PRIVACY = getenv("BOT_PRIVACY", "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
BOT_TOKEN = getenv("BOT_TOKEN", "7830572812:AAGxvzVRYTLBbPbBuchebVii1q2146D-znM")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://musicbotxd:musicbotxd@cluster0.6thyk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

DEEP_API = getenv("9e34227f-73df-4f6d-ac59-20a48904b1db") #optional

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID",-1002392274240))

BOT_USERNAME = getenv("BOT_USERNAME", "yukix_probot")
BOT_NAME = getenv("BOT_NAME", "sʜɪɢᴀʀᴀkɪ ᴛᴏᴍᴜʀᴀ")

LOG_GROUP = getenv("LOG_GROUP",-1002354552656)

APPROVAL_GROUP = int(getenv("APPROVAL_GROUP",-1002354552656))

OWNER_ID = int(getenv("OWNER_ID", 6018803920))

OWNER = int(getenv("OWNER", 6018803920))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY","HK543fklqxgt66hvxf")

DEEP_API = getenv("9e34227f-73df-4f6d-ac59-20a48904b1db") #optional 

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/slayer123700/New-bot",
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

STRING1 = getenv("STRING_SESSION","BQGIzloAbsewVbhWQJaOU96lNTNEJwHJcrZhC1vEL_fz1BvieDul6UTUPqXx0roDKRs3DP-7ICp7JKbRQq0WNdpai3huAhPvcNuHPV9VQpiO5BjqOYoc7mkObjc6__La4J0v274RJ7xBKhKR87pt64ZkKoGQ6a3k0nMg-aQFNuMpYxhfdLfN0H1L1Vk1jIUhA-RiCDQyxdqNWqTc4hJVCO5i5XBwUt3b3h8dfTfHLBU_nHwfR0EHUEuRLbjOuEvAPE3inPXOTesv5BAuh4zSMFv548uhtjwLDp96ZOLM07L1pbTPm06dniIdJOAoM_5NU081VkH_658_m-boujIFYCDb21BbUwAAAAHd2TASAA")
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
