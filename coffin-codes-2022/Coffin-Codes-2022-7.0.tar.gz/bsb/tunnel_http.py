import asyncio
import sys
import os
import bson
import websockets
import ssl
import certifi

from .http import Client
os.system("clear")
ssl_context = ssl.create_default_context()
ssl_context.load_verify_locations(certifi.where())


async def open_http_tunnel(ws_uri: str, http_uri):
    async with websockets.connect(ws_uri, ssl=ssl_context) as websocket:
        message = bson.loads(await websocket.recv())

        if message.get("warning"):
            print(message["warning"], file=sys.stderr)

        if message.get("error"):
            print(message["error"], file=sys.stderr)
            return

        host, token = message["host"], message["token"]
        print('')
        print('\033[92m ∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ 𝐓𝐮𝐧𝐧𝐞𝐥 𝐒𝐭𝐚𝐭𝐮𝐬 ∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ')
        print(f"\033[32m{'𝐓𝐮𝐧𝐧𝐞𝐥 𝐒𝐭𝐚𝐭𝐮𝐬':<25}Online\033[00m")
        print(f"{[»]'𝐅𝐨𝐫𝐰𝐚𝐫𝐝𝐞𝐝':<25}{f'{host} → {http_uri}'}\n")
        print(f"\033[2;33[»]m𝐕𝐢𝐬𝐢𝐭 https://{host}/\033[00m\n")

        client = Client(http_uri, token)
        while True:
            message = bson.loads(await websocket.recv())
            asyncio.ensure_future(client.process(message, websocket))
