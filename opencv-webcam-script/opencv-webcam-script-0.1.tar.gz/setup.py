#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: Yifu Zeng(曾逸夫)
# Mail: zyfiy1314@163.com
# Created Time:  2021-12-26
#############################################

from setuptools import setup, find_packages

setup(
    name = "opencv-webcam-script",
    version = "0.1",
    keywords = ["opencv","webcam"],
    description = "webcam opencv script",
    long_description = "This is a webcam opencv script, this script can be used to capture video frames.",
    license = "GPL-3.0 Licence",

    url = "https://gitee.com/CV_Lab/opencv-webcam",
    author = "Yifu Zeng",
    author_email = "zyfiy1314@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["opencv-python"]
)
