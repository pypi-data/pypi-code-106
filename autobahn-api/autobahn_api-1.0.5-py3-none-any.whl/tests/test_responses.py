#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.parse import urlparse

import responses
import requests
import pytest
import json


@responses.activate
def test_simulate_data_cannot_be_found():
    responses.add(
        responses.GET,
        "https://verkehr.autobahn.de/o/autobahn/A300/services/roadworks",
        json={"error": "No data exists for A300"},
        status=404
    )

    response = requests.get("https://verkehr.autobahn.de/o/autobahn/A300/services/roadworks")
    assert response.status_code == 404
    response_body = response.json()
    assert response_body["error"] == "No data exists for A300"


@responses.activate
def test_runtime_error():
    responses.add(
        responses.GET,
        "https://verkehr.autobahn.de/o/autobahn",
        body=RuntimeError("...")
    )
    with pytest.raises(RuntimeError) as ex:
        requests.get("https://verkehr.autobahn.de/o/autobahn")
    assert str(ex.value) == "..."


@responses.activate
def test_api_callback():

    def request_callback(request):
        request_url = request.url
        resp_body = {'value': generate_response_from(request_url)}
        return 200, {}, json.dumps(resp_body)

    responses.add_callback(
        responses.GET, "https://verkehr.autobahn.de/o/autobahn/A1/services/roadworks",
        callback=request_callback,
        content_type="application/json",
    )

    def generate_response_from(url):
        parsed_url = urlparse(url).path
        split_url = parsed_url.split("/")
        return f"You requested data for {split_url[3]} {split_url[4]} {split_url[5]}"

    response = requests.get("https://verkehr.autobahn.de/o/autobahn/A1/services/roadworks")
    assert response.json() == {"value": "You requested data for A1 services roadworks"}
