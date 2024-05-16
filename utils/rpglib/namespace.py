import utils.utils.registry


class Namespace(utils.utils.registry.Registry):
    def __init__(self, name):
        super().__init__()
        self.name = name
