from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "8439761"))
API_HASH = getenv("API_HASH", "aa3i949569078118031b99673860ede0")
OWNER_USERNAME = getenv("OWNER_USERNAME")
BOT_TOKEN = getenv("BOT_TOKEN","9877653742:AKR61TOx72pQEap0aHp56t9yQL5VUl-C7R0")
BOT_USERNAME = getenv("BOT_USERNAME", "TmcmusicBot")
BOT_NAME = getenv("BOT_NAME","Tmcmusicx")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "200"))
SESSION_NAME = getenv("SESSION_NAME", "BQCdZUPVqWdHudEeVSwMaYj2FoNB7x5LMGmFBTSe603Zo8shg0e_pxyqAJ59lxCvBblBOg-yn3nxNkzleIuv3q4poErGNQLNy2QL11BBjiZv2FK47xWn522ECLgWUg4Tnxhs_gkOZQjWkLkP1NWibeaxy0y5ufTaDS905u7ksMedBw_XBjeZHFkL4kLdRbnerhijU2UP1aJ0QfEN9nrSSDJj6NxxrFpg53nnlT4H9MXyZkGvMa9_CERrgCVlyz4bKcEOqw9RrQk6PhwnawfbkP3ESgFLT3FtBCvmZGFDTY2-1wFQzla9mK00KluI2n_266KZJqFnHLXIbR329-Yyy2ddbAMQnwA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! ? + . *").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5566939207").split()))
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/bhumiharsaurabh/katilmusicx",
)
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# You have to Enter the app name which you gave to identify your  Music Bot in Heroku.
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
