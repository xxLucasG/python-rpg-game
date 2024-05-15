class CommandArgumentType:
    def __init__(self, validation_fun):
        self.validation_fun = validation_fun

    def is_valid(self, arg):
        self.validation_fun(arg)


CommandArgumentType.STRING = CommandArgumentType(lambda arg: isinstance(arg, str))
CommandArgumentType.INTEGER = CommandArgumentType(lambda arg: isinstance(arg, int))
CommandArgumentType.DECIMAL = CommandArgumentType(lambda arg: isinstance(arg, float))
