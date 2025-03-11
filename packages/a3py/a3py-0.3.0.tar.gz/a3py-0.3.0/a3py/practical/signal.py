# -*- coding: utf-8 -*-
import signal
import sys
import heapq
from typing import Dict, List, Callable, Tuple
from itertools import count
from types import FrameType

from a3py.practical.singleton_meta import SingletonMeta

SignalHandlerType = Callable[[int, FrameType | None], None]


def exit_0_handler(*_, **__):
    sys.exit(0)


class PrioritizedSignalHandlerManager(metaclass=SingletonMeta):
    _counter = count()
    _handlers: Dict[int, List[Tuple[int, int, SignalHandlerType]]] = dict()
    _default_handler: Dict[int, SignalHandlerType | int | None] = dict()

    def _initialize_signal(self, signal_num: int):
        def _dispatcher(signum: int, frame: FrameType | None):
            heap = self._handlers[signum].copy()
            while heap:
                priority, _, handler = heapq.heappop(heap)
                handler(signum, frame)

        self._default_handler[signal_num] = signal.signal(signal_num, _dispatcher)

    def add_handler(self, signum: int, handler: SignalHandlerType, priority: int):
        if signum not in self._handlers:
            self._handlers[signum] = list()
            heapq.heappush(self._handlers[signum], (priority, next(self._counter), handler))
            self._initialize_signal(signum)
        else:
            heapq.heappush(self._handlers[signum], (priority, next(self._counter), handler))

    def remove_handler(self, signum: int, handler: SignalHandlerType):
        if signum in self._handlers:
            original_handlers = self._handlers[signum]
            self._handlers[signum] = [
                (priority, counter, h) for priority, counter, h in original_handlers if h != handler
            ]
            heapq.heapify(self._handlers[signum])

    def clear_handlers(self, signum: int):
        if signum in self._handlers:
            del self._handlers[signum]
            signal.signal(signum, self._default_handler[signum])

    def get_handlers(self, signum: int) -> List[Tuple[int, int, SignalHandlerType]]:
        return self._handlers.get(signum, list())
