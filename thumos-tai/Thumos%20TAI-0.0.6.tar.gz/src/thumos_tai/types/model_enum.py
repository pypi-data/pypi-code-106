from enum import Enum


class ModelType(str, Enum):
    TST = "TST"
    INCEPTION_TIME = "INCEPTION_TIME"
    XCM = "XCM"
    RES_NET = "RES_NET"
    FCN = "FCN"