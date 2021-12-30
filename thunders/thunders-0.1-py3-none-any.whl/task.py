# -*- coding: utf-8 -*-
# @author: leesoar

"""Thunder Download"""

import base64
import json
import subprocess
from typing import Iterable

import pyperclip


__all__ = ["Task", "GroupTask"]


class Task:
    def __init__(self, url: str, name: str = None):
        self.url = self.encode(url)
        self.name = name
        self.dir = ""
        self.origin_url = url

    @staticmethod
    def encode(url):
        encoded_url = base64.b64encode(f"AA{url}ZZ".encode()).decode()
        return f"thunder://{encoded_url}"

    def create(self):
        task = {
            "url": self.url,
            "dir": self.dir,
            "originUrl": self.origin_url,
        }
        self.name and task.update({
            "name": self.name,
        })
        return task


class GroupTask(list):
    dirname = "thunders"
    user_agent = "Bot"
    referer = ""
    min_version = "10.0.1.0"

    def __init__(self, name: str, thread_cnt=10):
        super().__init__()
        self.name = name
        self.thread_cnt = thread_cnt

    def __create(self):
        task = {
            "downloadDir": self.dirname,
            "installFile": "",
            "taskGroupName": self.name,
            "tasks": self,
            "minVersion": self.min_version,
            "userAgent": self.user_agent,
            "hideYunPan": "'1'",
            "threadCount": self.thread_cnt,
            "referer": self.referer,
        }
        return task

    def json(self):
        return json.dumps(self.__create(), ensure_ascii=False, separators=",:")

    def run(self, timeout=3):
        pyperclip.copy(self.__repr__())
        try:
            subprocess.check_output(["open", Task.encode("DummyLink/Copy-From-Clipboard")], timeout=timeout)
        except subprocess.CalledProcessError:
            print("[ERROR] Thunder version is wrong or not installed!")

    def append(self, task: Task):
        return super(GroupTask, self).append(task.create())

    def extend(self, tasks: Iterable[Task]):
        return super(GroupTask, self).extend(map(Task.create, tasks))

    def __str__(self):
        return f"thunders://{self.json()}"

    __repr__ = __str__
