from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "8439761"))
API_HASH = getenv("API_HASH", "aa3i949569078118031b99673860ede0")
OWNER_USERNAME = getenv("OWNER_USERNAME")
BOT_TOKEN = getenv("BOT_TOKEN","9877653742:AKR61TOx72pQEap0aHp56t9yQL5VUl-C7R0")
BOT_USERNAME = getenv("BOT_USERNAME", "musicctelebot")
BOT_NAME = getenv("BOT_NAME","PERFECT MUSIC")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "200"))
SESSION_NAME = getenv("SESSION_NAME", "isi sendiri")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1805855691").split()))
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Skyy112/musicsky",
)
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# You have to Enter the app name which you gave to identify your  Music Bot in Heroku.
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
