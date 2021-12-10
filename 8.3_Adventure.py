'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''

room_list = []
# create rooms and add to room_list
room = ['''You are in the Main hall. There are stairs going to the North going out of the building and stairs going
up, leading to more of the building. To the East there's hallway labeled West and to the East there is a 
hallway labeled West. However designed this place must've been pretty stupid. \n''', 13, 1, 12, 2]
room_list.append(room)
room = ['''You are in the West Hallway. There's not much here so you continue walking and realise it leads to another "
room. There's really nothing to do in here so you should probably just keep going to the next room. \n'''
        , None, None, 3, 0]
room_list.append(room)
room = ['''You are in the East Hallway.\n''', 13, 1, 2, 12]
room_list.append(room)
room = ["You are in a room with a guarded door.", 1, None, 6, None]
room_list.append(room)
room = ["You are in the Harry Potter Dining Hall.", 2, None, 7, None]
room_list.append(room)
room = ["You step into the void.", None, None, None, 6]
room_list.append(room)
room = ["You are in the Intersecting Hallway A.", 3, 5, 9, 7]
room_list.append(room)
room = ["You are in the Intersecting Hallway B.", 4, 6, 10, 8]
room_list.append(room)
room = ["You are in the NFT Room.", None, 7, None, None]
room_list.append(room)
room = ["You are in a warehouse with a ball pit in the middle.", 6, None, None, None]
room_list.append(room)
room = ["You are in the Sun Room.", 7, None, None, 11]
room_list.append(room)
room = ["You Walk into the woods.", None, 10, None, None]
room_list.append(room)
room = ["You are in a Basketball Court.", 0, None, None, None]
room_list.append(room)
room = ["You are Free of the Building.", None, None, None, None]
room_list.append(room)


current_room = 0
done = False
while not done:
    print()
    print(room_list[current_room][0])
    bing = input("Type N,E,W,S directions or q to quit - ")

    # NORTH
    if bing.lower() == "n" or bing.lower() == "north":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("you can't go that way")
        else:
            current_room = next_room

    # East
    elif bing.lower() == "e" or bing.lower() == "east":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("you can't go that way")
        else:
            current_room = next_room

    # South
    elif bing.lower() == "s" or bing.lower() == "south":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("you can't go that way")
        else:
            current_room = next_room

    # West
    elif bing.lower() == "w" or bing.lower() == "west":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("you can't go that way")
        else:
            current_room = next_room

    # Quit
    elif bing.lower() == "q" or bing.lower() == "quit":
        done = True

    # Stupid
    else:
        print("Not sure you understand what you are doing")
