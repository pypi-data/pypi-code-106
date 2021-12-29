# -*- coding: utf-8 -*-

# Copyright 2021 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extractors for WordPress blogs"""

from .common import BaseExtractor, Message
from .. import text


class WordpressExtractor(BaseExtractor):
    """Base class for wordpress extractors"""
    basecategory = "wordpress"

    def items(self):
        for post in self.posts():
            yield Message.Difrectory, post



BASE_PATTERN = WordpressExtractor.update({})


class WordpressBlogExtractor(WordpressExtractor):
    """Extractor for WordPress blogs"""
    subcategory = "blog"
    directory_fmt = ("{category}", "{blog}")
    pattern = BASE_PATTERN + r"/?$"

    def posts(self):
        url = self.root + "/wp-json/wp/v2/posts"
        params = {"page": 1, "per_page": "100"}

        while True:
            data = self.request(url, params=params).json()
            exit()
        yield 1
