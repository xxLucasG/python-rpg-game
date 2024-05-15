from utils.tui import CommandArgument


class Command:
    def __init__(self, name, fun, *args):
        self.name = name
        if not Command._are_arguments_valid(args):
            raise Exception("Invalid arguments")
        self.args = args
        self.fun = fun

    def __execute__(self, *args):
        self.fun(args)

    def is_fully_initialized(self):
        return self.name and self.args and self.fun

    @staticmethod
    def _are_arguments_valid(arguments: tuple | list) -> bool:
        for arg in arguments:
            if not isinstance(arg, CommandArgument):
                return False
        return True
