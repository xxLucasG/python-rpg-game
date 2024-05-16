from game.commands.exit import ExitCommand
from utils import CardinalDirection
from utils.rpglib import Namespace, Item
from utils.tui import CommandRegistry, Command
from commands import GoCommand, GetCommand
from utils.tui.commands.extensions import CardinalDirectionCommandArgumentType

VERSION = "1.0.1"


def showInstructions():
    #print a main menu and the commands
    print('''
        Welcome to your own RPG Game
        ============================
        Get to the Garden with a key and a potion.
        Avoid the monsters!
        Commands:
        go [direction]
        get [item]
    ''')


def showStatus():
    #print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'].identifier)
        print("---------------------------")


if __name__ == '__main__':
    namespace = Namespace('magicpaths')
    command_registry = CommandRegistry()

    go_command = GoCommand(namespace)
    get_command = GetCommand(namespace)
    exit_command = ExitCommand(namespace)

    command_registry.register_command(go_command)
    command_registry.register_command(get_command)
    command_registry.register_command(exit_command)

    inventory = []

    rooms = {
        'Hall': {CardinalDirection.SOUTH: 'Kitchen',
                 CardinalDirection.EAST: 'Dining Room',
                 'item': Item(namespace, 'key')
                 },
        'Kitchen': {CardinalDirection.NORTH: 'Hall',
                    'item': Item(namespace, 'monster')
                    },
        'Dining Room': {CardinalDirection.WEST: 'Hall',
                        CardinalDirection.SOUTH: 'Garden',
                        'item': Item(namespace, 'potion')
                        },
        'Garden': {CardinalDirection.NORTH: 'Dining Room'}
    }

    currentRoom = 'Hall'

    showInstructions()
    while True:
        showStatus()
        move = ''
        while move == '':
            move = input('>')
        move = move.lower().split()
        if move[0] == "exit":
            break
        if move[0] == 'go':
            direction = CardinalDirectionCommandArgumentType.get_parsed(move[1])
            if direction in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][direction]
            else:
                print('You can\'t go that way!')
        if move[0] == 'get':
            if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item'].identifier:
                inventory += [move[1]]
                print(move[1] + ' got!')
                del rooms[currentRoom]['item']
            else:
                print('Can\'t get ' + move[1] + '!')
        if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'].identifier:
            print('A monster has got you... GAME OVER!')
            break
        if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
            print('You escaped the house... YOU WIN!')
            break
