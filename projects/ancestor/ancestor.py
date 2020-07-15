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


def earliest_ancestor(ancestors, starting_node):
    stack = Stack()
    current_node = starting_node
    relationships = {}

    for pair in ancestors:
        parent, child = pair[0], pair[1]
        if child not in relationships:
            relationships[child] = set()
        relationships[child].add(parent)

    if starting_node in relationships:
        stack.push(relationships[current_node])
    else:
        return -1

    while True:
        relations = stack.pop()
        current_node = min(relations)
        if current_node not in relationships:
            return current_node
        else:
            stack.push(relationships[current_node])


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 1))  # , 10)
print(earliest_ancestor(test_ancestors, 2))  # , -1)
print(earliest_ancestor(test_ancestors, 3))  # , 10)
print(earliest_ancestor(test_ancestors, 4))  # , -1)
print(earliest_ancestor(test_ancestors, 5))  # , 4)
print(earliest_ancestor(test_ancestors, 6))  # , 10)
