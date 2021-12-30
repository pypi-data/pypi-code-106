# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_heweather']

package_data = \
{'': ['*'], 'nonebot_plugin_heweather': ['templates/*']}

install_requires = \
['httpx>=0.18.0,<1.0.0', 'nonebot-plugin-htmlrender>=0.0.2']

setup_kwargs = {
    'name': 'nonebot-plugin-heweather',
    'version': '0.4.0.1',
    'description': 'Get Heweather information and convert to pictures',
    'long_description': '# nonebot-plugin-heweather\n\n获取和风天气信息并转换为图片\n\n# 和风天气API图标信息编号变化\n\n由于和风天气图标ID和图标发生变化\n* 在2021.11.30前创建的API将保持原有信息\n* 之后创建的API将使用新版图标信息\n* 旧版API使用`pip install nonebot-plugin-heweather==0.2.1`进行安装\n* 新版API图标已更新，可直接安装\n* 图标适配还没做，打算重写，先等等吧～\n\n# 安装\n\n直接使用 `pip install nonebot-plugin-heweather` 进行安装\n\n然后在 `bot.py` 中 写入 `nonebot.load_plugin("nonebot_plugin_heweather")`\n\n# 指令\n\n`天气+地区` 或 `地区+天气`\n\n# 配置\n\n## apikey 必须配置 环境配置\n\n```\nQWEATHER_APIKEY = xxx\n```\n\n## 是否使用商业版 可选 环境配置\n\n- 不添加则默认开发版\n\n```\nQWEATHER_COMMERCIAL = true\n```\n\n## 字体文件 可选 环境配置\n\n```\nQWEATHER_FONT = "./data/heweather/font.ttc"\n```\n\n- 使用 truetype 字体\n- 建议使用微软雅黑\n\n## 图标文件 可选 环境配置\n\n**注意**末端的`/`, 代表目录！\n\n```\nQWEATHER_ICON_DIR = "./data/heweather/icon/"\n```\n\n## 背景文件 可选 环境配置\n\n\n默认路径`./data/heweather/backgroud.png`\n\n```\nQWEATHER_BACKGROUD = "./data/heweather/backgroud.png"\n```\n\n\n',
    'author': 'kexue',
    'author_email': 'x@kexue.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0.0',
}


setup(**setup_kwargs)
