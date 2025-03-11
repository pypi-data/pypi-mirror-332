# -*- coding: utf-8 -*-
from threading import Lock
from typing import Dict, Type


class SingletonMeta(type):
    _instances: Dict[Type, object] = dict()
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]
