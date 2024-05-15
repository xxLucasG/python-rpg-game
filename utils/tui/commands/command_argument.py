from utils.tui import CommandArgumentType


class CommandArgument:
    def __init__(self,
                 name: str,
                 argtype: CommandArgumentType,
                 description: str = "",
                 required: bool = True):
        self.name = name
        self.argtype = argtype
        self.description = description
        self.required = required
