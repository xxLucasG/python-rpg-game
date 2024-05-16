from utils.rpglib import Item
from .. import command_argument_types


class ItemCommandArgumentType(command_argument_types.CommandArgumentType):
    def __init__(self, namespace):
        self.namespace = namespace
        super().__init__(self._validation_function)

    def _validation_function(self, arg):
        if not isinstance(arg, Item):
            raise Exception("Argument must be a item")
        if self.namespace.has(arg) is None:
            raise Exception("Argument must be a registered item inside the namespace")
        return True
