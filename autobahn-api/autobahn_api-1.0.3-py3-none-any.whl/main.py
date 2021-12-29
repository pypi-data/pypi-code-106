#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
A Python wrapper for the Autobahn API
provided by https://bund.dev/
Version: 1.0
Python 3.10
Date created: December 28th, 2021
Date modified: December 29th, 2021
"""

import argparse
import logging
from pprint import pprint

from src.autobahn_api import data
from src.autobahn_api import info

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def get_parser() -> argparse.ArgumentParser:
    """
    Create a command line parser.
    Returns:
        argparse.ArgumentParser: Created parser
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-r",
        "--roadworks",
        type=str,
        required=False,
        help="list of roadworks"
    )

    parser.add_argument(
        "-p",
        "--parking",
        type=str,
        required=False,
        help="list of service areas"
    )

    parser.add_argument(
        "-v",
        "--version",
        required=False,
        action="store_true",
        help="show the version"
    )

    return parser


def main():
    """
    Invoke the parser and evaluate the result.
    """
    parser = get_parser()
    args = parser.parse_args()

    if args.roadworks:
        data_type = "roadworks"
        endpoint_manager = data.EndpointManager(args.roadworks, data_type)
        roadworks_data = endpoint_manager.fetch_data()
        pprint(roadworks_data)
    elif args.parking:
        data_type = "parking_lorry"
        endpoint_manager = data.EndpointManager(args.parking, data_type)
        parking_lorry_data = endpoint_manager.fetch_data()
        pprint(parking_lorry_data)
    elif args.version:
        info.app_info()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
