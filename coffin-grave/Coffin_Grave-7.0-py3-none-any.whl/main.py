import asyncio
import sys
from getpass import getuser

import click
import os 
from .tunnel_http import open_http_tunnel
from .tunnel_tcp import open_tcp_tunnel
from . import __version__

os.system("clear")
@click.group()
def main():
    pass


@main.command()
@click.argument('port')
@click.option('-s', '--subdomain', default='')
@click.option('--host', default='open.jprq.io')
def http(**kwargs):
    host = kwargs['host']
    port = kwargs['port']
    username = kwargs['subdomain'] or getuser()
    print('\033[92m ∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ ᄅ0ᄅᄅ ∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ')
    print("\033[91m[»] 𝑪𝒐𝒇𝒇𝒊𝒏 𝑪𝒐𝒅𝒆𝒔 𝑽7")
    print("\033[94m[»] BₛB₋Dₑᵥₑₗₒₚₑᵣₛ")
    print("\033[94m[»] We do everything like a sir !!!")
    print("\033[95m[»] Press Ctrl+C to quit.")

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            open_http_tunnel(
                ws_uri=f'wss://{host}/_ws/?username={username}&port={port}&version={__version__}',
                http_uri=f'http://127.0.0.1:{port}',
            )
        )
    except KeyboardInterrupt:
        print("\n\033[31m[»] 𝑪𝒐𝒇𝒇𝒊𝒏 𝑪𝒐𝒅𝒆𝒔 𝑽7") tunnel closed\033[00m")


@main.command()
@click.argument('port', type=click.INT)
@click.option('--host', default='tcp.jprq.io')
def tcp(**kwargs):
    host = kwargs['host']
    port = kwargs['port']

    #print(f"\n\033[1;35mjprq : {__version__}\033[00m \033[34m{'Press Ctrl+C to quit.':>60}\n")

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            open_tcp_tunnel(remote_server_host=host, ws_uri=f'wss://{host}/_ws/', local_server_port=port)
        )
    except KeyboardInterrupt:
        #print("\n\033[31mjprq tunnel closed\033[00m")
        sys.exit(1)


if __name__ == '__main__':
    main()
