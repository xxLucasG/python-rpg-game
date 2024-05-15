class EventListener:
    def __init__(self, on_trigger):
        self.on_trigger = on_trigger

    def trigger(self, *args):
        self.on_trigger(*args)