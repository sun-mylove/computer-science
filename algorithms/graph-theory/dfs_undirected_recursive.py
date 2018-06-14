import timeit

start = timeit.default_timer()


def undirected_graph_dfs(e):
    global ver_traverse_stack
    global ver_visited

    while len(ver_traverse_stack) != 0:
        ver_picked = ver_traverse_stack.pop()

        vertices = e[ver_picked]

        for vertex in vertices:
            if vertex not in ver_visited:
                ver_visited.append(vertex)
                ver_traverse_stack.append(vertex)
                undirected_graph_dfs(e)


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

# a list to keep track of all visited vertices to ensure
# we don't process DFS for already visited vertex; and
# this will be the output of DFS
ver_visited = []

# a STACK data structure to pick elements to apply DFS
ver_traverse_stack = []

# initializing with starting vertex
ver_visited.append(starting_vertex)
ver_traverse_stack.append(starting_vertex)

# calling DFS algorithm
undirected_graph_dfs(edges)

# Output of DFS
print "DFS Order:", ver_visited

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
# ['A', 'B', 'F', 'G', 'C', 'J', 'I', 'H', 'D', 'E']
