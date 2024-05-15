from utils import CardinalDirection
from utils.tui import Command, CommandArgument, CommandArgumentType
from utils.tui.commands.extensions import CardinalDirectionCommandArgumentType


class GoCommand(Command):

    @staticmethod
    def _get_1st_argument():
        return CommandArgument("direction", CardinalDirectionCommandArgumentType())

    @staticmethod
    def _command_functionality(direction: CardinalDirection):
        ...

    def __init__(self):
        super().__init__("go",
                         GoCommand._command_functionality,
                         GoCommand._get_1st_argument())
