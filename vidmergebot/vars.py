from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Vars:
    CACHE_TIME = int(config("CACHE_TIME", default=5))
    DOWN_PATH = f"{getcwd()}/vidmergebot/downloads"
    BOT_TOKEN = config("BOT_TOKEN","")
    BOT_ID = BOT_TOKEN.split(":")[0]
    APP_ID = int(config("API_ID","6534707"))
    API_HASH = config("API_HASH","4bcc61d959a9f403b2f20149cbbe627a")
    WORKERS = int(config("WORKERS", default=16))
    STREAMTAPE_API_PASS = config("STREAMTAPE_API_PASS")
    STREAMTAPE_API_USERNAME = config("STREAMTAPE_API_USERNAME")
    MESSAGE_DUMP = int(config("MESSAGE_DUMP"))
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/ !").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="animedualaudiozippercartoonist")
    AUTH_CHANNEL = config("AUTH_CHANNEL", default=-1001560385250)
    OWNER_ID = int(config("OWNER_ID", default=1430593323))
    CAPTION = config("CAPTION", default="By @animedualaudiozippercartoonist")
    VERSION = config("VERSION", default="v1.1 - Stable")
    STREAMTAPE_DEFAULT = config("STREAMTAPE_DEFAULT", default=None, cast=config.boolean)
    BOT_USERNAME = config("BOT_USERNAME")
    DB_URI = config("DB_URI","mongodb+srv://Uploader:Uploader@cluster0.ba0ppxa.mongodb.net/?retryWrites=true&w=majority")
    MAX_VIDEOS = int(config("MAX_VIDEOS", default=10))
    JOIN_CHECK = config("JOIN_CHECK", default=None, cast=config.boolean)
    MAX_NON_JOIN_USAGE = int(config("MAX_NON_JOIN_USAGE", default=2))
    MAX_JOIN_USAGE = int(config("MAX_JOIN_USAGE", default=2))
    LIMIT_USER_USAGE = config("LIMIT_USER_USAGE", default=None, cast=config.boolean)
