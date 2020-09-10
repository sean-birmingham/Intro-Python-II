from room import Room
from player import Player

import emoji
from termcolor import colored
from colorama import init
from time import sleep
from os import system, name

init()

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

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
player = Player('Sean', room['outside'])

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


def game_intro():
    global game
    clear()
    while game == False:
        print(
            f'Welcome, {player.name}! Please type "play" to start game or "help" for instructions')
        command = input('> ').lower()
        instructions = {"movement:": ["n", "s", "e",
                                      "w"], "other commands:": "q to quit"}

        if command == 'play':
            game = True
            clear()
            sleep(.2)
        elif command == 'help':
            for k, v in instructions.items():
                print(k, v)
        else:
            print(colored('Wrong command doofus!', 'red'))


game_intro()

while game == True:
    print(
        f"Location: {player.current_room.name}\n")
    print(f"{player.current_room.description}")

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
    elif command == 'q':
        print(
            f'Sorry to see you go {emoji.emojize(":worried_face:")}')
        sleep(1)
        clear()
        game = False
        game_intro()
    else:
        print(colored('Wrong command doofus!', 'red'))
