import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "1975516"))
API_HASH = getenv("API_HASH", "419c5fbaab800b44c89e436920ca0455")
BOT_TOKEN = getenv("BOT_TOKEN", "5400412639:AAF2Rs-Q1uBn9AP6ktu3o_N-yrGJNLfThbw")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "AgDEaPROSsNvqguHyxXkNzjV4g9OmdNtTFTCrqXv6blgUk3dGm5AXN7VFiDatlWqyxhw019W307IiMrL6D_j_RYt3O659t-sx_gRQyPKZ9tixkXEuzJddCCZeCmc7rDK-wWB-eU37qd9qO-ywrV_QnTh7aeIz-dmY47RnOl2_mhuMowFNwOk19XrUSmmRV8eAepwFsgSFOHlfK-2JD8QD9aZqLIzkQ8ky9DTFrH8m7xajyQNNiXbuv16WJuEJfVKevT0PuWODgzLupykvyj1BNZ97ex3beW6rkkb2ky2lPq51lt1V-i1su-vhPGJPw1vSUv3943RcvsBk74R-cSr5pI4AAAAAUtZP_UA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
