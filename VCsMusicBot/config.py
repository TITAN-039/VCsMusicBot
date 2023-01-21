import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "1AZWarzsBu1aU99sni0y8ZHEmUUV0oPk9JpnBVa6vi2eYqg-ag87VFGkGfQNyaK3bv7X-7JJBh1OoZn7LHP07KBVXXTQDGeoJWmZOZKjKrpPcwLHxwPzezu5z6dgOPt-HWjybzrCx7bjwPYqzrMoKigQhRB7KzB3Dcl6qcisCNUjDKbYZrb1PrmMlSeksEgnqsMpKdWq-wE7fu6ti6mYShVx1gunv5Swl17Em4R4ekXyu7O8YKvuulRQOzijJQnQ6uzmGnKD2--JadzrhMlMgTMuOHcsZoGbEgTIDX3WIljnxB0jlMSEslM-ZXa7ReNPNqF9NQAG9Ls8N8ko14rxXxlQSELCZAs0=")
BOT_TOKEN = getenv("BOT_TOKEN", "5731586246:AAFJ9yVZ26B_DU9a5z4BpoqAOkgzGHrU78Q")
BOT_NAME = getenv("BOT_NAME", "F4R X MUSIX")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TITANS_DARK_WORLD")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/cf19dda907391656338eb.png")
admins = {}
API_ID = int(getenv("API_ID", "23785459"))
API_HASH = getenv("API_HASH", "4ad74412e0cff337b063c655bd72807d")
BOT_USERNAME = getenv("BOT_USERNAME", "F4R_X_MUSIC_BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "VCsMusicPlayer")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "FRIENDS_FOUR_REAL")
PROJECT_NAME = getenv("PROJECT_NAME", "VCsMusicPlayer")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/ZauteKm/VCsMusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5912734719").split()))
