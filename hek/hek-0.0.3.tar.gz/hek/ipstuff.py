import socket
from exceptions import *


def siteip(url: str):
    try:
        if len(url) != 0: # check url length if not 0
            hostname = socket.gethostbyname(url) # grab host url
            return hostname
        else:
            raise LengthError("Invalid url length") # Invalid url length error.
    except:
        raise SiteHostNameRequestError("Request host name error") # Request host name error
