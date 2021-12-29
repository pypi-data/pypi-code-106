#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from autobahn_api import main

import pytest


@pytest.fixture()
def create_parser():
    """
    Create a parser
    """
    parser = main.get_parser()
    yield parser


def test_evaluate(create_parser):
    """
    Test if the given arguments will be parsed.

    Args:
        create_parser: The created parser
    """
    args_version = create_parser.parse_args(['--version'])
    args_parking = create_parser.parse_args(['--parking', 'A1'])
    args_roadworks = create_parser.parse_args(['--roadworks', 'A1'])

    assert args_version.version is True
    assert args_parking.parking == "A1"
    assert args_roadworks.roadworks == "A1"
