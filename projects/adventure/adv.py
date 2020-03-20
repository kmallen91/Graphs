from room import Room
from player import Player
from world import World
from stack import Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()
# print(room_graph[0][1].items())
player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


# check if room in directions (N, E, S, W)
# check if neighbors have been visited (possibly second array for 'undiscovered')
# add undiscovered rooms to stack, go thru undiscovered
# once undiscovered is empty, move to previous room, recheck

# parse the map graph to get all rooms and their directions
room_dict = {}

for i in range (len(room_graph)):
    room_dict[i] = room_graph[i][1]

# print(room_dict)
# print("player room:", player.current_room.id)


s = Stack()
visited = set()
path = []
neighbors = player.current_room.get_exits()

# push room 0 onto stack
s.push(0)

while len(visited) < len(room_dict):
    # id of current room in stack
    id = s.stack[-1]
    # add current room to visited    
    visited.add(id)
    # set current room
    current_room = room_dict[id]
    # array to see if room has not been found
    undiscovered = []
    # store undiscovered rooms in relation to current room
    for direction, room_id in current_room.items():
        if room_id not in visited:
            undiscovered.append(room_id)
    # assign the next room
    if len(undiscovered) > 0:
        next_room = undiscovered[0]
        s.push(next_room)
    # if we reached a dead end, back track
    else:
        s.pop()
        next_room = s.stack[-1] 
    # survey rooms, if next room equals room id then add to path
    for direction, adjacent_id in current_room.items():
        if adjacent_id == next_room:
            traversal_path.append(direction)      
    
  



# create path from room, once hit dead end, iterate through path and append opposite directions in order to move backwards
# create helper function to take an array and return 'swapped' values (S for N, E for W, etc)



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
