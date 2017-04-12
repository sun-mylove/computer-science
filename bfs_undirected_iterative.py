import timeit
from collections import deque

start = timeit.default_timer()


def bfs_undirected(e, s):

    # dictionary to hold the distances of each vertex from starting vertex
    distances = {}

    # initializing the distances dictionary with "-1" value for all vertices;
    # the BFS algorithm will overwrite with correct value; if not, the vertex
    # is deemed to be unreachable from staring vertex
    for ver in xrange(1, n + 1):
        distances[ver] = -1

    # a list to keep track of all visited vertices to ensure
    # we don't process BFS for already visited vertex
    ver_visited = set([])

    # a QUEUE data structure to pick elements to apply BFS
    ver_traverse_queue = deque([])

    # initialize below data structures that drive the BFS
    ver_visited.add(s)
    ver_traverse_queue.append(s)
    distances[s] = 0

    # below BFS algorithm is run considering each vertex as starting
    # vertex until all the vertices are done
    while len(ver_traverse_queue) != 0:
        ver_picked = ver_traverse_queue.popleft()

        vertices = e[ver_picked]

        for vertex in vertices:
            if vertex not in ver_visited:
                ver_visited.add(vertex)
                ver_traverse_queue.append(vertex)
                distances[vertex] = distances[ver_picked] + 1

    return distances


# program begins here
# read number of vertices - n; and
# number of edges - m
n, m = map(int, raw_input().strip().split(' '))

# a dictionary to hold all edges with vertex as key;
# and a list of heads of its edges as value
edges = {}

# run loop to read all edges
for edge in xrange(m):
    u, v = map(int, raw_input().strip().split(' '))

    # adding edge to dictionary with tail as key;
    # and head appended to value list
    try:
        edges[u].append(v)
    except KeyError:
        edges[u] = [v]

    # run below try except block only if its un-directional graph
    try:
        edges[v].append(u)
    except KeyError:
        edges[v] = [u]

# read the starting vertex
starting_vertex = int(raw_input().strip())

# calling BFS algorithm that calculates distance of each vertex from
# starting vertex
print bfs_undirected(edges, starting_vertex)

print timeit.default_timer() - start

#################################
# input format:
# n, m
# u1 v1
# u2 v2
# s
# example:
# 4 3
# 1 2
# 2 3
# 3 1
# 2
# Output:
# {1: 1, 2: 0, 3: 1, 4: -1}
