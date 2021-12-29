#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Fetch roadworks list
Python 3.10
Date created: December 28th, 2021
"""

import requests
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

URL = "https://verkehr.autobahn.de/o/autobahn"


class EndpointManager:
    """
    This class manages the api endpoints
    -> Create an endpoint url
    -> Retrieve the associated data
    """
    def __init__(self, data_id: str, data_type: str):
        self.data_id = data_id  # A1
        self.data_type = data_type  # roadworks

    def __repr__(self):
        rep = self.data_id + ", " + self.data_type
        return rep

    def create_url(self) -> str:
        """
        Creates the endpoint based on the chosen data
        Returns: Endpoint url

        """
        if self.data_type == "roadworks":
            data_url = URL + f"/{self.data_id}/services/roadworks"
            return data_url
        else:
            data_url = URL + f"/{self.data_id}/services/parking_lorry"
            logger.debug(data_url)
            return data_url

    def fetch_data(self) -> str:
        """
        Connect to the server and recieve the data
        (roadworks or service areas)
        Returns: Recieved data
        """
        endpoint = self.create_url()

        # Connect to the server
        try:
            response = requests.get(endpoint)
        except OSError as e:
            print("Error: {0}".format(e))
            return None

        # Check if the request is successfull
        # and receive data
        if response.status_code == 200:
            logger.debug("Status 200, OK")
            return response.json()
        else:
            print("JSON data request not successfull!")
            return None
