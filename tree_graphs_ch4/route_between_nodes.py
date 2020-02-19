class Graph:
    def __init__(self):
        self._vertices = []

    def add_vertex(self, node):
        self._vertices.append(node)

    def add_vertices(self, list):
        for n in list:
            self._vertices.append(n)

class Node:
    def __init__(self, name):
        self._name = name
        self._children = []

    def add_child(self, child):
        self._children.append(child)
        child._children.append(self)
       
def find_path(graph, start, end):
    path = []
    seen = []

    dfs_search(start, end, path, seen)
    return path

def dfs_search(start, end, path, seen):
    if start in seen:
        return
    seen.append(start)
    path.append(start)
    if start == end:
      return True
    else:
        for v in start._children:
            if dfs_search(v, end, path, seen):
                return True
    path.pop()
    return False

def print_path(path):
    for p in path:
        print(p._name)

nodes = [Node('A'), Node('B'), Node('C'), Node('D'), Node('E'), Node('F')]
graph = Graph()
graph.add_vertices(nodes)

nodes[0].add_child(nodes[1])
nodes[0].add_child(nodes[2])
nodes[2].add_child(nodes[3])
nodes[2].add_child(nodes[4])
nodes[4].add_child(nodes[5])
nodes[5].add_child(nodes[1])

path = find_path(graph, nodes[5], nodes[1])
print_path(path)
