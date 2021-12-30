# -*- coding: utf-8 -*-
# @Time    : 7/3/2021 9:04 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: config.py
# @Software: PyCharm

"""
ClickHouse：

# 寻找clickhouse镜像
> docker search clickhouse
# 拉取镜像
> docker pull yandex/clickhouse-server
# 启动clickhouse容器
> docker run -d --name clickhouse-server --volume=/Users/joseph/Dropbox/code/qtrader/examples/data/clickhouse:/var/lib/clickhouse --ulimit nofile=262144:262144 -p 8123:8123 -p 9000:9000 yandex/clickhouse-server

"""
FUTU_GATEWAY = {
    "broker_name": "FUTU",
    "broker_account": "715823",
    "host": "127.0.0.1",
    "port": 11111,
    "pwd_unlock": 314159,
}

IB_GATEWAY = {
    "broker_name": "IB",
    "broker_account": "715823",
    "host": "127.0.0.1",
    "port": 11111,
    "pwd_unlock": 314159,
}

BACKTEST_GATEWAY = {
    "broker_name": "BACKTEST",
    "broker_account": "",
    "host": "",
    "port": -1,
    "pwd_unlock": -1,
}

GATEWAYS = {
    "Futu": FUTU_GATEWAY,
    "IB": IB_GATEWAY
}

TIME_STEP = 60000  # 设置事件框架监测步长 ms

DATA_PATH = {
    "k1m": "/Users/joseph/Dropbox/code/stat-arb/data/k_line/K_1M", # "k1m" is must have
    "capdist": "/Users/joseph/Dropbox/code/stat-arb/data/capital_distribution",
}

DATA_MODEL = {
    "k1m": "Bar",
    "capdist": "CapitalDistribution"
}

DB = {
    "sqlite3": "/Users/joseph/Dropbox/code/stat-arb/data/sqlite3"
}

ACTIVATED_PLUGINS = ["analysis", "sqlite3"]

CLICKHOUSE = {
    "host": "localhost",
    "port": 9000,
    "user": "default",
    "password": ""
}