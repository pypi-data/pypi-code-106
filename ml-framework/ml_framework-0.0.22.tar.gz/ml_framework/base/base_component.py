from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional, List


class Runner(ABC):
    _next_runner: Optional[Runner] = None
    _prev_runner: Optional[List[Runner]] = None

    @abstractmethod
    def set_next(self, runner: Runner) -> Runner:
        pass

    @abstractmethod
    def run(self, request) -> Optional[str]:
        return None

    @abstractmethod
    def do_fn(self, request):
        pass


class BaseComponent(Runner):
    def __init__(self, **kwargs):
        [setattr(self, k, kwargs[k]) for k in kwargs]

    def set_next(self, runner: Runner) -> Runner:
        self._next_runner = runner
        return runner

    def do_fn(self, request):
        [fn(request) for fn in getattr(self, "do_fns", [])]

    def __named_variable_runner(self, func_name):
        requested_func = getattr(self, func_name, None)
        if requested_func is not None:
            variable_dict = {k: getattr(self, k) for k in requested_func.__code__.co_varnames}  # type: ignore
            requested_func(**variable_dict)  # type: ignore

    def run(self, request: Any) -> Optional[str]:
        self.__named_variable_runner("run_fn")
        self.do_fn(request)
        self.__named_variable_runner("end_callback")

        if self._next_runner:
            # ? 1): File I/O is quite slow, so do we write all the results of the components
            # ? into artifact files or propegate the results over the components
            # ? 2): Using both with Multithreading and I/O only for backup and if that component
            # ? is missing...
            # TODO: agreed on that the data will be propegate though the pipeline and write out to artifact
            # TODO: in end of the components. For speed up try to use multipithreading for file I/O and
            # TODO: multiprocessing for calculations beside the components, and defined dependencies between
            # TODO: component (for parallelize them).
            if self._next_runner._prev_runner is not None:
                self._next_runner._prev_runner.append(self.__class__)  # type: ignore
            else:
                self._next_runner._prev_runner = [self.__class__]  # type: ignore
            return self._next_runner.run(request)
        return None
