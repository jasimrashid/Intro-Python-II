from room import Room
from player import Player
from item import Item, LightSource

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

# Add new rooms for level 2
room.update({
    'moat': Room("make a wrong move and you're toast", "avoid the crocodiles" ),
    'waiting_area': Room("there's a guard here", "how do you deal with him?"),
    'reception': Room("many different paths to take", "you can go upstairs, north, south, east or west!")
})


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
#Level 2 map
room['moat'].e_to = room['waiting_area']
room['waiting_area'].e_to = room['reception']
room['reception'].w_to = room['waiting_area']


# Add items to rooms
room['outside'].items.append(Item(name='sword', description = 'This can kill another player if there are multiple players and you encounter one in a room'))
room['foyer'].items.append(Item(name='scroll', description='This will give you a clue'))
room['foyer'].items.append(Item(name='sword', description = 'This can kill another player if there are multiple players and you encounter one in a room'))
room['foyer'].items.append(LightSource(name='torch', description = 'This will help you see more items in the room'))
room['treasure'].items.append(Item(name='gem', description = 'You can trade this for something else'))
room['treasure'].items.append(LightSource(name='match', description = 'You can only use this once'))
room['narrow'].items.append(Item(name='coin', description='5 points'))

# Classify rooms that have lighting
room['outside'].is_light = True
room['foyer'].is_light = True
room['overlook'].is_light = True

# Main
# Make a new player object that is currently in the 'outside' room.
player = Player(name = 'Jasim', current_room = room['outside'])

# Loop begins
while True:

# # * Prints the current room name
    print()
    print("Score: ", player.score)
    print("Current location: ", player.current_room)
    print()
    print("Items in your inventory:")
    player.print_items()
    print()
    # items = player.current_room.get
    for i in player.current_room.items:
        if isinstance(i, LightSource) == True:
            player.current_room.lightsource = True

    items_names = player.current_room.get_items_names()

    if (player.current_room.is_light == True or player.current_room.lightsource == True):
        print("Items in room:")
        player.current_room.print_items()
    else:
        print("Room is dark.")
    # print()
    print(f"""Type 'n', 's', 'e' or 'w' to move in any direction. 
    Type 'get <item name>' or 'pick <item name>' to pick up an item.
    Type 'drop <item name>' to drop an item in a room
    If you drop a lightsource in a dark room, it will illuminate the room.

    Press 'q' to quit.
    """)

    command = input("> ").split(',')

    # TODO: refactor below
    if command[0] == 'bp':
        breakpoint()
    
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

    elif (command[0].startswith('get ') or command[0].startswith('pick ')):
        command0 = command[0].split(' ')
        if (player.current_room.lightsource == False or player.current_room.is_light == False):
            print("Good luck finding that in the dark")
        if len(command0) == 1:
            print('Please input a valid value')
        else:
            if(command0[1] in items_names):
                pos = items_names.index(command0[1])
                player.current_room.items[pos].on_take()
                player.add_item(player.current_room.items.pop(pos))
            else:
                print('No matching item')

    elif command[0].startswith('drop '):
        command0 = command[0].split(' ')
        if len(command0) == 1:
            print('Please input a valid value')
        else:
            if(command0[1] in items_names):
                pos = items_names.index(command0[1])
                player.items[pos].on_drop()
                player.current_room.add_item(player.items.pop(pos))
            else:
                print('No matching item')
    
    else:
        print("Please provide a valid input")
    # elif command[0] == '2':
    #     items = player.get_items()
    #     print("Items in inventory:\n",items)

# open items:
# try catch block?



