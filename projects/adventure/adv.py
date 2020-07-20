from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

#! Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = ["n"]


s = Stack()
s.push(player.current_room.id)
visited = []
world_graph = dict()

while len(visited) < len(room_graph):
    #     room = s.pop()
    #     if room not in visited:
    #         print(room)
    #         visited.append(room)
    #         for direction in player.current_room.get_exits():
    #             if direction not in visited[room]:
    #                 visited[room][direction] = "?"

    # print(world_graph)

"""
    # get room ID player is currently in
    room = player.current_room.id
    print("current", room)
    # get what direction you just moved
    last_direction = traversal_path[-1]
    # see if room has been visited
    if room not in visited:
        # if room not visited, add to dictionary
        visited[room] = dict()
        # populate visited dictionary with all exits
        for direction in player.current_room.get_exits():
            if direction not in visited[room]:
                visited[room][direction] = "?"
"""

# add all room directions to stack
# move player into new room
# add move to traversal_path
# check if it is the end then backtrack

# print("-" * 5)
# print(visited[room][direction])
# if visited[room][direction] == "?":
#     traversal_path += [direction]
#     s.push(traversal_path)
#     player.travel(direction)
# else:
#     print(visited[room])

# if room in visited:
# for direction in visited[room]:
# if visited[room][direction] == "?":
#     traversal_path.append(direction)
#     player.travel(direction)
#     new_room = player.current_room.id
#     print("new", new_room)
#     visited[room][direction] = new_room
#     s.push([traversal_path])
#     break
# break

# print(traversal_path)
# print("visited", visited)

# path = s.pop()
#     # move player
#     move_direction = path[-1]
#     player.travel(move_direction)
#     # add move the the traversal
#     traversal_path.append(move_direction)
#     # what if dead end and no exits... backtrack
#     if room not in visited:
#         print("visited", visited)
#         visited[room] = dict()
#         for direction in player.current_room.get_exits():
#             visited[room][direction] = "?"
#             s.push(path + [direction])
#         print("-" * 5)

# print(traversal_path)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
