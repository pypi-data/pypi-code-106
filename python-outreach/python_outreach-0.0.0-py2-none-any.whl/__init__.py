#!/usr/bin/env python3

import sys
import json
import argparse

import singer
from singer import metadata
from singer.catalog import write_catalog

from python_outreach.client import OutreachClient
from python_outreach.discover import discover
from python_outreach.sync import sync

LOGGER = singer.get_logger()

REQUIRED_CONFIG_KEYS = [
    'start_date',
    'client_id',
    'client_secret',
    'redirect_uri',
    'refresh_token'
]


def check_auth(or_client):
    LOGGER.info('Testing authentication')
    try:
        or_client.get(path='stages', endpoint='stages')
    except:
        raise Exception('Error testing Outreach authentication')


@singer.utils.handle_top_exception(LOGGER)
def main():
    parsed_args = singer.utils.parse_args(REQUIRED_CONFIG_KEYS)
    catalog = parsed_args.catalog if parsed_args.catalog else discover()

    if parsed_args.discover:
        write_catalog(catalog)
    else:
        with OutreachClient(parsed_args.config) as or_client:
            check_auth(or_client)
            sync(or_client, parsed_args.config, catalog, parsed_args.state, parsed_args.config['start_date'])
