import os
import enum
import datetime

from ml_framework.logger.misc import get_fn_ln


class LoggerLevel(enum.Enum):
    CRITICAL = 0
    WARNING = 1
    INFO = 2
    DEBUG = 3

    def __eq__(self, other):
        return self.value == other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value


class Logger:
    def __init__(self, level=LoggerLevel.WARNING):
        self._level = level

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, new_level):
        self._level = new_level

    def __msg(self, message, filename, ln, level):
        if level <= self.level:
            print(
                f"{datetime.datetime.now()}[{level.name}] - {os.path.basename(filename)}:{ln} - {message}"
            )
        else:
            pass

    def set_level(self, level):
        if level.lower() == "critical":
            self.level = LoggerLevel.CRITICAL
        elif level.lower() == "info":
            self.level = LoggerLevel.INFO
        elif level.lower() == "debug":
            self.level = LoggerLevel.DEBUG
        else:
            self.level = LoggerLevel.WARNING

    def critical(self, message):
        filename, ln = get_fn_ln()
        self.__msg(
            message=message, filename=filename, ln=ln, level=LoggerLevel.CRITICAL
        )

    def warning(self, message):
        filename, ln = get_fn_ln()
        self.__msg(message=message, filename=filename, ln=ln, level=LoggerLevel.WARNING)

    def info(self, message):
        filename, ln = get_fn_ln()
        self.__msg(message=message, filename=filename, ln=ln, level=LoggerLevel.INFO)

    def debug(self, message):
        filename, ln = get_fn_ln()
        self.__msg(message=message, filename=filename, ln=ln, level=LoggerLevel.DEBUG)


logger = Logger()
