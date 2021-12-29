#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.autobahn_api.data import EndpointManager

URL = "https://verkehr.autobahn.de/o/autobahn"


def test_create_endpoint_manager():
    endpoint_manager = EndpointManager("A1", "roadworks")
    assert repr(endpoint_manager) == "A1, roadworks"


def test_create_roadworks_url():
    endpoint_manager = EndpointManager("A1", "roadworks")
    result = endpoint_manager.create_url()
    assert result == "https://verkehr.autobahn.de/o/autobahn/A1/services/roadworks"


def test_create_parking_url():
    endpoint_manager = EndpointManager("A1", "parking_lorry")
    result = endpoint_manager.create_url()
    assert result == "https://verkehr.autobahn.de/o/autobahn/A1/services/parking_lorry"
