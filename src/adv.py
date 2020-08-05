from room import Room
from player import Player

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

# Add items to rooms
room['outside'].add_item('sword', 'This can kill another player if there are multiple players and you encounter one in a room')
room['foyer'].add_item('scroll_1', 'This will give you a clue')
room['foyer'].add_item('sword', 'This can kill another player if there are multiple players and you encounter one in a room')
room['treasure'].add_item('gem', 'You can trade this for something else')

#
# Main
#
# Make a new player object that is currently in the 'outside' room.

player = Player(name = 'Jasim', current_room = room['outside'])

# Write a loop that:
# breakpoint()
while True:

# # * Prints the current room name
    print("Current location: ", player.current_room)
    # print("**")
    print("Items in room:")
    player.current_room.get_items()
    print()
    print(f"""Press 'N', 'S', 'E', 'W' to move in any direction. 
    If there are items that can be picked up, press '1' to pick it up.
    Press '2' to see items you have.
    Press 'q' to quit.
    """)

    # breakpoint()
# * Prints the current description (the textwrap module might be useful here).
    
# * Waits for user input and decides what to do.

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    command = input("> ").split(',')

    if command[0] == 'q':
        break
    elif command[0] == 'n':         
        if hasattr(player.current_room, 'n_to') == False:
            print('Cannot move north. Try again. \n')
        else:
            player.current_room = player.current_room.n_to
        # check if player can move to the north
        # if there is, set that north room to the player's location
    elif command[0] == 's':
        if hasattr(player.current_room, 's_to') == False:
            print('Cannot move south. Try again. \n')
        else:
            player.current_room = player.current_room.s_to

    elif command[0] == 'e':
        if hasattr(player.current_room, 'e_to') == False:
            print('Cannot move east. Try again. \n')
        else:
            player.current_room = player.current_room.e_to
        

    elif command[0] == 'w':
        if hasattr(player.current_room, 'w_to') == False:
            print('Cannot move west. Try again. \n')
        else:
            player.current_room = player.current_room.w_to




# open items:
# try catch block?

