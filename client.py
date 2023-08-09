from pyrogram import Client
from dotenv import load_dotenv
import os

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = str(os.getenv("API_HASH"))
raw_proxy = os.getenv("PROXY")

parsed_proxy = {
    "scheme": "",  # "socks4", "socks5" and "http" are supported
    "hostname": "",
    "port": 0,
    "username": "",
    "password": ""
}

if not (api_id or api_hash):
    raise Exception("You have to pass both API_ID and API_HASH env variables")


def proxyParser(proxy):
    start_host = 0
    for i in range(len(proxy)):
        if proxy[i] == ":" and i < 7:
            parsed_proxy["scheme"] = proxy[0: i]
        elif proxy[i] == "/":
            start_host = i + 1
        elif proxy[i] == ":" and i > 7:
            parsed_proxy["hostname"] = proxy[start_host: i]
            parsed_proxy["port"] = int(proxy[i + 1:])

    del parsed_proxy["password"]
    del parsed_proxy["username"]

    print(parsed_proxy)


proxyParser(raw_proxy)

app = Client("auto-reaction", api_id, api_hash)
