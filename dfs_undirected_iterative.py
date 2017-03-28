import timeit

start = timeit.default_timer()


def undirected_graph_dfs(e, s):
    global dfs_order

    # a list to keep track of all visited vertices to ensure
    # we don't process DFS for already visited vertex
    ver_visited = set([])

    # a STACK data structure to pick elements to apply DFS
    ver_traverse_stack = []

    # initializing with starting vertex
    ver_visited.add(s)
    ver_traverse_stack.append(s)

    while len(ver_traverse_stack) != 0:

        ver_picked = ver_traverse_stack.pop()
        dfs_order.append(ver_picked)

        vertices = e[ver_picked]

        for vertex in vertices:
            if vertex not in ver_visited:
                ver_visited.add(vertex)
                ver_traverse_stack.append(vertex)


# PROGRAM BEGINS HERE
# read number of vertices - n; and
# number of edges - m
n, m = map(int, raw_input().strip().split(' '))

# a dictionary to hold all edges
edges = {}

# run loop to read all edges
for edge in xrange(m):
    u, v = raw_input().strip().split(' ')

    # adding edge to dictionary with tail as key;
    # and all outgoing heads appended to value list
    try:
        edges[u].append(v)
    except KeyError:
        edges[u] = [v]

    try:
        edges[v].append(u)
    except KeyError:
        edges[v] = [u]

# read the starting vertex
starting_vertex = raw_input().strip()

# a list to keep track of the vertices visited applying DFS
dfs_order = []

# calling DFS algorithm
undirected_graph_dfs(edges, starting_vertex)

# Output of DFS
print "DFS Order:", dfs_order

print timeit.default_timer() - start

#################################
# input format:
# n, m
# u1 v1
# u2 v2
# s
# example:
# A B
# A E
# B F
# C G
# D E
# D H
# F G
# F I
# F J
# G J
# H I
# A
# Output:
# ['A', 'E', 'H', 'I', 'F', 'J', 'G', 'C', 'D', 'B']
