from room import Room
from player import Player
from world import World
from collections import Counter

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


#! You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
back_direction = {
    "n": "s",
    "e": "w",
    "s": "n",
    "w": "e"
}
#! Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = list()
world_graph = dict()
visited = list()
visited.append(player.current_room.id)
# * add current room and exits
world_graph[player.current_room.id] = dict()
for direction in player.current_room.get_exits():
    world_graph[player.current_room.id][direction] = "?"

i = 1
room_graph_length = len(room_graph)
if room_graph_length >= 12:
    room_graph_length += 1
while len(visited) < room_graph_length:
    # print(f"move: {i} <------")
    i += 1
    # * get room player is currently in
    current_room = player.current_room
    #! print("CURRENT --->", current_room.id, "<---")
    # * random DFT
    choices = [choice for choice in world_graph[player.current_room.id]
               if world_graph[player.current_room.id][choice] == "?"]
    backtrack_directions = list()
    # print("CHOICES", choices)
    if not choices:
        # print("DEAD END", "*"*20)
        #! print("GRAPH", world_graph)
        q = Queue()
        q.enqueue([current_room.id])
        back_visited = set()
        backtrack = list()
        while q.size() > 0:
            path = q.dequeue()
            # print("PATH", path)
            v = path[-1]
            if v not in back_visited:
                if "?" in world_graph[v].values():
                    # print("PATH FOUND!!!", path)
                    backtrack = path
                    break

                back_visited.add(v)
                # Then add A PATH TO its neighbors to the back of the queue
                for n in world_graph[v]:
                    q.enqueue(path + [world_graph[v][n]])

        while len(backtrack) > 1:
            for k, v in world_graph.items():
                if k == backtrack[0]:
                    backtrack = backtrack[1:]
                    # print("BACK", backtrack)
                    if len(backtrack) == 0:
                        break
                    for k1, v1 in v.items():
                        if v1 == backtrack[0]:
                            # print("V1", v1)
                            backtrack_directions.append(k1)
                            player.travel(k1)
                            traversal_path.append(k1)
                            current_room = player.current_room
        #! print("BACKTRACKED ROOM", player.current_room.id)

    # print(world_graph[player.current_room.id])
    # print("HERE", [choice for choice in world_graph[player.current_room.id]
    #                if world_graph[player.current_room.id][choice] == "?"])
    # travel_direction = random.choice(newChoices)
    # print(travel_direction)
    # break
    # if len(visited) >= len(room_graph):
    #     break
    print("VISITED:", len(visited))

    travel_direction = random.choice([choice for choice in world_graph[player.current_room.id]
                                      if world_graph[player.current_room.id][choice] == "?"])

    # * move player
    #! print("TRAVEL:", travel_direction)
    player.travel(travel_direction)

    # * add direction to traversal path
    traversal_path.append(travel_direction)
    new_room = player.current_room
    #! print("NEW:", new_room.id)

    # print("BEFORE", world_graph)
    # * mark new room as visited and update previous room direction
    visited.append(new_room)
    world_graph[current_room.id][travel_direction] = new_room.id

   # * add new room to graph with unknown surrounding rooms
    if new_room.id not in world_graph:
        #! print("NEW-->", new_room.id)
        world_graph[new_room.id] = dict()
        for direction in new_room.get_exits():
            world_graph[new_room.id][direction] = "?"

    # * update room directions (THIS IS NOT FOR BACKTRACK)
    # if len(backtrack_directions) == 0:
    world_graph[player.current_room.id][back_direction[travel_direction]
                                        ] = current_room.id
    # else:
    #     # current_room.id is not DEAD END it is what i backtracked too
    #     world_graph[player.current_room.id][back_direction[travel_direction]
    #                                         ] = player.current_room.id
    #     pass

    #! print("AFTER", world_graph)
# print("PATH", traversal_path)


#! TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph) - 2:
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)+2} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
#! UNCOMMENT TO WALK AROUND
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
