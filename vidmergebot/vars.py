import os
from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Vars:
    CACHE_TIME = int(config("CACHE_TIME", default=5))
    DOWN_PATH = f"{getcwd()}/vidmergebot/downloads"
    BOT_TOKEN = os.environ.get("BOT_TOKEN","5442493323:AAGE585VqW2Rjn8p7fTamBdyiSsg9dktdgE")
    BOT_ID = BOT_TOKEN.split(":")[0]
    APP_ID = int(os.environ.get("API_ID","6534707"))
    API_HASH = os.environ.get("API_HASH","4bcc61d959a9f403b2f20149cbbe627a")
    WORKERS = int(os.environ.get("WORKERS", default=16))
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS")
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME")
    MESSAGE_DUMP = int(os.environ.get("MESSAGE_DUMP","100"))
    PREFIX_HANDLER = os.environ.get("PREFIX_HANDLER", default="/ !").split()
    SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", default="-1001306818456")
    AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", default=-1001560385250)
    OWNER_ID = int(os.environ.get("OWNER_ID", default=1430593323))
    CAPTION = os.environ.get("CAPTION", default="By @animedualaudiozippercartoonist")
    VERSION = os.environ.get("VERSION", default="v1.1 - Stable")
    STREAMTAPE_DEFAULT = os.environ.get("STREAMTAPE_DEFAULT", default=None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    DB_URI = os.environ.get("DB_URI","mongodb+srv://Uploader:Uploader@cluster0.ba0ppxa.mongodb.net/?retryWrites=true&w=majority")
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", default=10))
    JOIN_CHECK = os.environ.get("JOIN_CHECK", default=None)
    MAX_NON_JOIN_USAGE = int(os.environ.get("MAX_NON_JOIN_USAGE", default=2))
    MAX_JOIN_USAGE = int(os.environ.get("MAX_JOIN_USAGE", default=2))
    LIMIT_USER_USAGE = os.environ.get("LIMIT_USER_USAGE", default=None)
