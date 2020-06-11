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


class Graph:
    def __init__(self):
        self.vertices = {}

    # add verts
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    # add edges

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex doesn't exist")

    # get neighboors for a vert

    def get_neighboors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        q = Queue()
        q.enqueue(starting_vertex_id)

        visited = set()

        while q.size() > 0:
            v = q.dequeue()

            if v not in visited:
                print(v)
                visited.add(v)
                for n in self.get_neighboors(v):
                    q.enqueue(n)


g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')

g.add_edge('B', 'C')
g.add_edge('B', 'A')
g.add_edge('A', 'C')
g.add_edge('C', 'B')
g.add_edge('C', 'A')

print(g.get_neighboors('B'))
print(g.get_neighboors('C'))
print("-"*10)
print(g.vertices)
g.bft('B')
print("-"*10)
g.bft('A')
