import logging
import sys
from datetime import datetime

from pytz import timezone
from prometheus_client import start_http_server


class LoggerMixin(object):
    @property
    def logger(self):
        try:
            return self._logger
        except AttributeError:
            return logging


class ProcessLogger(object):
    def __init__(self,
                 level=logging.INFO):
        self._logger = logging.getLogger(self.__class__.__name__)
        self._logger.setLevel(level)
        logging.Formatter.converter = self.custom_time

    @property
    def logger_formatter(self):
        return logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def add_file_handler(self,
                         filename='logger.log'):
        handler = logging.FileHandler(filename)
        handler.setFormatter(self.logger_formatter)
        self._logger.addHandler(handler)

    def add_rotating_file_handler(self,
                                  filename='logger.log',
                                  max_bytes=50*1024*1024,
                                  backup_count=2):
        handler = logging.handlers.RotatingFileHandler(filename,
                                                       maxBytes=max_bytes,
                                                       backupCount=backup_count)
        handler.setFormatter(self.logger_formatter)
        self._logger.addHandler(handler)

    def add_stdout_handler(self):
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(self.logger_formatter)
        self._logger.addHandler(handler)

    @staticmethod
    def custom_time(*args):
        tz = timezone('Asia/Tehran')
        converted = datetime.now(tz=tz)
        return converted.timetuple()


class MetricsServer(LoggerMixin):
    def __init__(self,
                 port=9100):
        try:
            start_http_server(port)
            self.logger.info(f'METRICS SERVER: INITIALIZED ON PORT {port}')
        except OSError:
            self.logger.info(f'METRICS: SERVER ALREADY RUNNING ON PORT {port}')
