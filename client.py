from pyrogram import Client
from dotenv import load_dotenv
from urllib.parse import urlparse
import os

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = str(os.getenv("API_HASH"))
raw_proxy = os.getenv("PROXY")

urlparse(raw_proxy)

proxy = {
    "scheme": urlparse(raw_proxy).scheme,
    "hostname": urlparse(raw_proxy).hostname,
    "port": urlparse(raw_proxy).port,
}

if not (api_id or api_hash):
    raise Exception("You have to pass both API_ID and API_HASH env variables")


app = Client("auto-response", api_id, api_hash, proxy=proxy)
