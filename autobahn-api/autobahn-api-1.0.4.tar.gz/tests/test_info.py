#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from autobahn_api import info


def test_version():
    assert info.VERSION == "1.0.4"
