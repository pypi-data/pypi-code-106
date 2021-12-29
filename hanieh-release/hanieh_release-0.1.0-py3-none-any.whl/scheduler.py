from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.blocking import BlockingScheduler

from skeleton.monitoring import LoggerMixin


class Scheduler(LoggerMixin):
    def __init__(self):
        self._scheduler = BlockingScheduler(executors={'default': ThreadPoolExecutor(10)})

    def add_job(self,
                func,
                misfire_grace_time=600,
                trigger='interval',
                seconds=60):
        self._scheduler.add_job(func=func,
                                misfire_grace_time=misfire_grace_time,
                                trigger=trigger,
                                seconds=seconds)

    def start_scheduler(self):
        self._scheduler._start()

    def shutdown_scheduler(self):
        self._scheduler.shutdown()
