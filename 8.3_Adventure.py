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
hallway labeled West. However designed this place must've been pretty stupid. \n''', None, 1, None, 2, None]
room_list.append(room)
room = ['''You are in the West Hallway. There's not much here so you continue walking and realise it leads to another "
room around the corner. There's really nothing to do in here so you should probably just keep going to the next room. 
\n''', None, None, 3, 0, None]
room_list.append(room)
room = ['''You are in the East Hallway. At the end of the hallway there's a painting of ____. Around the corner there is
another room. Doesn't seem like there's much to do in this room, maybe the next room will be exiting.\n''', None, 0,
        4, None, None]
room_list.append(room)
room = ['''You are in a room with a guarded door. On either side of the door there is two stone statues on either side
of the double doors. You start to reach for the door and you see the statue on the left turn it's head slowly. \n''',
        1, None, 6, None, '''Would you like to reach for the door?''']
room_list.append(room)
room = ['''You are in what looks to be the Harry Potter Dining Hall. There are four differently colored tables, each 
full of kids wearing matching robes. At the front of the dining hall there's a row of old people all watching as kids
go up and put a hat on their head. As you walk past the evil looking kids you question how good of a school a place
like this could be.\n''', 2, None, 7, None, '''Do you wish to be sorted into one of the four houses?''']
room_list.append(room)
room = ['''You take a step into the void. There's nothing that you can see around you except nothingness in every
direction.\n''', None, None, None, 6, '''You step farther into the void hesitantly, unsure what to make of this room.
As soon as you take your third step Ninja Tyler Blevins appears, clearly having just eaten a Taki as fire spirals around
him. You realise you are not in any simple void, you have entered the Taki dimension and it's seriously intense. So
intense you are blown back into the hallway. The door you just came out of disappears in a fiery swirl of intensity.
It's hard to know if you'll ever experience something so intense ever again.''']
room_list.append(room)
room = ['''You are in the Intersecting Hallway A. You see rooms to the North, South, and East. To the West you see a
river that goes to the other intersecting hallway.\n''', 3, 5, 9, 7, None]
room_list.append(room)
room = ['''You are in the Intersecting Hallway B. You see rooms to the North, South, and West. To the East you see a
river that goes to the other intersecting hallway.\n''', 4, 6, 10, 8, None]
room_list.append(room)
room = ['''You are in the NFT Room. All around you are pictures of gross monkeys and other weird pieces of "art." As you
look around, you can't help but think, "Why would anyone pay for this?"\n''', None, 7, None, None, '''There's really not
you can do in this room, it's pretty useless. Just pointlessly large amounts of money being wasted on bad art. But
before you leave, you take out your phone and take a picture of the room, it's a free way to get the same thing so why
not.''']
room_list.append(room)
room = ['''You are in a warehouse with a kids ball pit in the middle. The smell of sadness and despair wafts towards you
and causes you to take a step back. As you approach the ball pit, you see a fine layer of dust across the balls, clearly
never being touched in the last several years.\n''', 6, None, None, None, '''You jump into the ball pit without a second
of thought. It's not very deep so you heart your legs a little bit.''']
room_list.append(room)
room = ['''You are in the Sun Room. There is a couch with a coffee table in front of it and a dinner table set for four 
beside it. The room seems like a nice calming place to sit and relax. Outside the windows on every wall, you see an 
unmoving forest full of trees but with no wildlife.\n''', 7, None, None, 11]
room_list.append(room)
room = ['''You walk into the woods. But as soon as you take your first step out you realise this isn't actually a
forest, it's Dust II the map from the hit game CSGO. The door that was just there behind you is gone and you are left in
this desert hellscape alone. Off in the distance you can hear some incomprehensible screaming drawing closer.\n''',
        None, 10, None, None]
room_list.append(room)
room = ['''You are in a Basketball Court. In the center is basketball super star LeBron James from the hit movie Space 
Jam: A New Legacy. He's just standing there, dribbling his basketball. No words are spoken but you can feel his energy
radiating off of him, challenging you to play him in basketball.\n''', 0, None, None, None]
room_list.append(room)
room = ['''You are Free of the Building. Was it all worth it? You must now go back to your meaningless, non-miraculus, 
life. In the building you had adventure, excitement, and puzzlement, it is really worth leaving behind?''', None, None,
        None, None]
room_list.append(room)


current_room = 0
done = False
while not done:
    print()
    print(room_list[current_room][0])
    bing = input("Type N,E,W,S directions to move, I to interact, or Q to quit - ")

    # NORTH
    if bing.lower() == "n" or bing.lower() == "north":
        next_room = room_list[current_room][1]
        if next_room is None:
            print("you can't go that way")
        else:
            current_room = next_room

    # East
    elif bing.lower() == "e" or bing.lower() == "east":
        next_room = room_list[current_room][2]
        if next_room is None:
            print("you can't go that way")
        else:
            current_room = next_room

    # South
    elif bing.lower() == "s" or bing.lower() == "south":
        next_room = room_list[current_room][3]
        if next_room is None:
            print("you can't go that way")
        else:
            current_room = next_room

    # West
    elif bing.lower() == "w" or bing.lower() == "west":
        next_room = room_list[current_room][4]
        if next_room is None:
            print("you can't go that way")
        else:
            current_room = next_room

    # Quit
    elif bing.lower() == "q" or bing.lower() == "quit":
        done = True

    # Interact
    elif bing.lower() == "i" or bing.lower() == "interact":
        if room_list[current_room][5] is None:
            print("There's not much to do in this so you just pace around for a little bit.")
        else:
            print(room_list[current_room][5])

    # Stupid
    else:
        print("Not sure you understand what you are doing")
