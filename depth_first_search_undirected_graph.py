import timeit

start = timeit.default_timer()


def undirected_graph_dfs(e):
    global n
    global ver_traverse_stack
    global ver_visited
    global topological_sort

    while len(ver_traverse_stack) != 0:
        ver_picked = ver_traverse_stack.pop()

        try:
            vertices = e[ver_picked]
        except KeyError:
            continue

        for vertex in vertices:
            if vertex not in ver_visited:
                ver_visited.append(vertex)
                ver_traverse_stack.append(vertex)
                undirected_graph_dfs(e)

        topological_sort[n] = ver_picked
        n -= 1

# program begins here
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

# initializing with starting vertex
ver_visited.append(starting_vertex)

# a STACK data structure to pick elements to apply DFS
ver_traverse_stack = []

# initializing with starting vertex
ver_traverse_stack.append(starting_vertex)

# dictionary that holds the topological sort order of vertices
topological_sort = {}

# calling DFS algorithm
undirected_graph_dfs(edges)

# Output of DFS
print ver_visited

# Output of topological order of vertices
print [topological_sort[k] for k in sorted(topological_sort.keys())]

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
# ['A', 'B', 'F', 'I', 'H', 'D', 'E', 'G', 'J', 'C']
