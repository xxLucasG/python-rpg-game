from utils import CardinalDirection
from utils.tui import CommandArgumentType


class CardinalDirectionCommandArgumentType(CommandArgumentType):
    cardinal_directions = {"north": CardinalDirection.NORTH,
                           "south": CardinalDirection.SOUTH,
                           "east": CardinalDirection.EAST,
                           "west": CardinalDirection.WEST}

    def __init__(self):
        super().__init__(validation_fun=CardinalDirectionCommandArgumentType._validation_function)

    @staticmethod
    def _validation_function(arg):
        if not isinstance(arg, str):
            raise Exception("Argument must be a string")
        if CardinalDirectionCommandArgumentType.get_parsed(arg) is None:
            raise Exception("Argument must be a cardinal direction")
        return True

    @staticmethod
    def get_parsed(arg):
        if arg in CardinalDirectionCommandArgumentType.cardinal_directions:
            return CardinalDirectionCommandArgumentType.cardinal_directions[arg]
        return None
