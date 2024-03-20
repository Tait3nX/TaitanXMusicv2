from TaitanX.core.bot import Taitan
from TaitanX.core.dir import dirr
from TaitanX.core.git import git
from TaitanX.core.userbot import Userbot
from TaitanX.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Taitan()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
