# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['quart_discord', 'quart_discord.models']

package_data = \
{'': ['*']}

install_requires = \
['Async-OAuthlib>=0.0.9,<0.0.10',
 'PyJWT>=2.3.0,<3.0.0',
 'cachetools>=5.0.0,<6.0.0',
 'oauthlib>=3.1.1,<4.0.0',
 'quart>=0.16.2,<0.17.0']

setup_kwargs = {
    'name': 'quart-discord-any',
    'version': '2.2.1b3',
    'description': 'Discord OAuth2 extension for Quart using modern Discord Libraries.',
    'long_description': '# Quart-Discord\n[![PyPI](https://img.shields.io/pypi/v/Quart-Discord?style=for-the-badge)](https://pypi.org/project/Quart-Discord/) [![Read the Docs](https://img.shields.io/readthedocs/quart-discord?style=for-the-badge)](https://quart-discord.readthedocs.io/en/latest/) \n\nDiscord OAuth2 extension for Quart using py-cord, nextcord, or the deprecated discord.py.\n\n\n### Installation\nTo install current latest release use one of the following commands:\n\nFor py-cord: (My recommendation)\n```sh\npython3 -m pip install Quart-Discord-any[pycord]\n```\n\nFor nextcord:\n```sh\npython3 -m pip install Quart-Discord-any[nextcord]\n```\n\nFor the deprecated discord.py:\n```sh\npython3 -m pip install Quart-Discord-any[discordpy]\n```\n\n# You _MUST_ install one of the extras!\n\n\n### Basic Example\n```python\nfrom quart import Quart, redirect, url_for\nfrom quart_discord import DiscordOAuth2Session, requires_authorization, Unauthorized\n\napp = Quart(__name__)\n\napp.secret_key = b"random bytes representing quart secret key"\n\napp.config["DISCORD_CLIENT_ID"] = 490732332240863233    # Discord client ID.\napp.config["DISCORD_CLIENT_SECRET"] = ""                # Discord client secret.\napp.config["DISCORD_REDIRECT_URI"] = ""                 # URL to your callback endpoint.\napp.config["DISCORD_BOT_TOKEN"] = ""                    # Required to access BOT resources.\n\ndiscord = DiscordOAuth2Session(app)\n\n\n@app.route("/login/")\nasync def login():\n    return await discord.create_session()\n\t\n\n@app.route("/callback/")\nasync def callback():\n    await discord.callback()\n    return redirect(url_for(".me"))\n\n\n@app.errorhandler(Unauthorized)\nasync def redirect_unauthorized(e):\n    return redirect(url_for("login"))\n\n\t\n@app.route("/me/")\n@requires_authorization\nasync def me():\n    user = await discord.fetch_user()\n    return f"""\n    <html>\n        <head>\n            <title>{user.name}</title>\n        </head>\n        <body>\n            <img src=\'{user.avatar_url}\' />\n        </body>\n    </html>"""\n\n\nif __name__ == "__main__":\n    app.run()\n```\n\nFor an example to the working application, check [`test_app.py`](tests/test_app.py)\n\n\n### Requirements\n* Quart\n* Async-OAuthlib\n* cachetools\n\n\n### Documentation\nHead over to [documentation] for full API reference. \n\n\n[documentation]: https://quart-discord.readthedocs.io/en/latest/\n',
    'author': 'Philip Dowie',
    'author_email': 'philip@jnawk.nz',
    'maintainer': 'William Hatcher',
    'maintainer_email': 'william@memotic.net',
    'url': 'https://github.com/Memotic/Quart-Discord-any',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
