from room import Room
from player import Player
from item import Item

import emoji
from termcolor import colored
from colorama import init
from time import sleep
from os import system, name

init()

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item('Sword', 'This is a sword'), Item('Torch', 'This is a torch')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('leaflet', 'This is a leaflet')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input('Please enter your name: ')
player = Player(player_name, room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


game = False


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# main menu


def game_intro():
    global game
    clear()
    while game == False:
        print(
            f'Welcome, {player.name}! Please type "play" to start game, "help" for instructions, or "q" to quit')
        command = input('> ').lower()
        instructions = {"movement: ": ["n", "s", "e",
                                       "w"], "open inventory:": "i or inventory", "pick up item:": "get [item] or take [item]", "drop item:": "drop [item]", "quit:": "q"}

        if command == 'play':
            game = True
            clear()
            sleep(.2)
        elif command == 'help':
            for k, v in instructions.items():
                print(k, v)
        elif command == 'q':  # exit menu
            print('Bye Bye!')
            exit()
        else:
            print(colored('Wrong command doofus!', 'red'))


game_intro()

# game
while game == True:
    print(
        f"{player.current_room.name}:\n{player.current_room.description}\n")

    command = input('> ').lower()

    if command == 'n':
        try:
            player.current_room = player.current_room.n_to
        except:
            print(colored("Can't go this way!", 'red'))
    elif command == 'e':
        try:
            player.current_room = player.current_room.e_to
        except:
            print(colored("Can't go this way!", 'red'))
    elif command == 's':
        try:
            player.current_room = player.current_room.s_to
        except:
            print(colored("Can't go this way!", 'red'))
    elif command == 'w':
        try:
            player.current_room = player.current_room.w_to
        except:
            print(colored('Wrong direction!', 'red'))
    elif command == 'look':
        player.current_room.look()
    elif command.split()[0] == "take" or command.split()[0] == "get":
        for item in player.current_room.items:
            if command.split()[1] == item.name.lower():
                player.take_item(item)

    elif command.split()[0] == "drop":
        for item in player.inventory:
            if command.split()[1] == item.name.lower():
                player.drop_item(item)
            else:
                print(f"You don't have {command.split()[1]}")

    elif command == 'i' or command == 'inventory':
        player.show_inventory()
    elif command == 'q':
        print(
            f'Sorry to see you go {emoji.emojize(":worried_face:")}')
        sleep(1)
        clear()
        # exit and go to menu
        game = False
        game_intro()

    else:
        print(colored('Wrong command doofus!', 'red'))
