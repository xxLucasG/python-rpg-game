from utils.rpglib import Item
from utils.tui import CommandArgument, Command
from utils.tui.commands.extensions import ItemCommandArgumentType


class GetCommand(Command):
    @staticmethod
    def _get_1st_argument(namespace):
        return CommandArgument("item", ItemCommandArgumentType(namespace))

    @staticmethod
    def _command_functionality(item: Item):
        ...

    def __init__(self, namespace):
        super().__init__("go",
                         GetCommand._command_functionality,
                         namespace,
                         GetCommand._get_1st_argument(namespace))
