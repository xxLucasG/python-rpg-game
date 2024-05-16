from utils import Registry


class Namespace(Registry):
    def __init__(self, name):
        super().__init__()
        self.name = name
