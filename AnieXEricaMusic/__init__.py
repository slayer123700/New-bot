from AnieXEricaMusic.core.bot import AMBOT
from AnieXEricaMusic.core.dir import dirr
from AnieXEricaMusic.core.git import git
from AnieXEricaMusic.core.userbot import Userbot
from AnieXEricaMusic.misc import dbb, heroku

from .logging import LOGGER

# Optional APIs
from .platforms import *

# Extra Exports
from AnieXEricaMusic.utils.cache import admin_cache
from AnieXEricaMusic.mongo.dbfilter import filter_collection

# Initialize Core Functions
dirr()
git()
dbb()
heroku()

# Initialize Bots
app = AMBOT()
userbot = Userbot()

# Initialize APIs
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
