import sys

from utils import CardinalDirection
from utils.tui import Command, CommandArgument, CommandArgumentType
from utils.tui.commands.extensions import CardinalDirectionCommandArgumentType


class ExitCommand(Command):

    @staticmethod
    def _command_functionality(direction: CardinalDirection):
        sys.exit(0)

    def __init__(self, namespace):
        super().__init__("exit",
                         ExitCommand._command_functionality,
                         namespace)
