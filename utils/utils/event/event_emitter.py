import threading
from collections import defaultdict


class EventEmitter:
    def __init__(self):
        self.listeners_lock = threading.Lock()
        self.listeners = defaultdict(lambda: list())

    def emit(self, name, *args):
        result = True
        self.listeners_lock.acquire()
        for listener in self.listeners[name]:
            if listener.trigger(*args) == False:
                result = False
                break
        self.listeners_lock.release()
        return result

    def on(self, name, listener):
        self.listeners[name].append(listener)

    def off(self, name, listener):
        with self.listeners_lock:
            self.listeners[name].remove(listener)
