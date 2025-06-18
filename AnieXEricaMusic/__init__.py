from AnieXEricaMusic.core.bot import AMBOT
from AnieXEricaMusic.core.dir import dirr
from AnieXEricaMusic.core.git import git
from AnieXEricaMusic.core.userbot import Userbot
from AnieXEricaMusic.misc import dbb, heroku
from AnieXEricaMusic.logging import LOGGER

# Initialize core utilities
dirr()
git()
dbb()
heroku()

# Initialize main app and userbot
app = AMBOT()
userbot = Userbot()

# Load all platform APIs
from AnieXEricaMusic.platforms import (
    AppleAPI,
    CarbonAPI,
    SoundAPI,
    SpotifyAPI,
    RessoAPI,
    TeleAPI,
    YouTubeAPI
)

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

# Constants
JOIN_UPDATE_GROUP = 70
FILTERS_GROUP = 70
parse_mode = "Markdown"

# Export cache and filter modules
from AnieXEricaMusic.utils.cache import admin_cache
from AnieXEricaMusic.mongo.filters import filter_collection
