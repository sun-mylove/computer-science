import timeit

start = timeit.default_timer()


def directed_graph_dfs(e, s):
    global n
    global topological_sort
    global dfs_order

    # a list to keep track of all visited vertices to ensure
    # we don't process DFS for already visited vertex
    ver_visited = []

    # a STACK data structure to pick elements to apply DFS
    ver_traverse_stack = []

    # initializing with starting vertex
    ver_visited.append(s)
    ver_traverse_stack.append(s)

    while len(ver_traverse_stack) != 0:
        child = 0
        ver_picked = ver_traverse_stack[-1]

        if ver_picked not in dfs_order:
            dfs_order.append(ver_picked)

        try:
            vertices = e[ver_picked]
        except KeyError:
            topological_sort[n] = ver_traverse_stack.pop()
            n -= 1
            continue

        for vertex in vertices:
            if vertex not in ver_visited:
                ver_visited.append(vertex)
                ver_traverse_stack.append(vertex)
                child += 1

        if child == 0:
            topological_sort[n] = ver_traverse_stack.pop()
            n -= 1

# program begins here
# read number of vertices - n; and
# number of edges - m
n, m = map(int, raw_input().strip().split(' '))

# a dictionary to hold all edges
edges = {}

# run loop to read all edges
for edge in xrange(m):
    u, v = map(int, raw_input().strip().split(' '))

    # adding edge to dictionary with tail as key;
    # and all outgoing heads appended to value list
    try:
        edges[u].append(v)
    except KeyError:
        edges[u] = [v]

# read the starting vertex
starting_vertex = int(raw_input().strip())

# dictionary that holds the topological sort order of vertices
topological_sort = {}

# a list to keep track of the vertices visited applying DFS
dfs_order = []

# calling DFS algorithm
directed_graph_dfs(edges, starting_vertex)

print "dfs order", dfs_order

print [topological_sort[k] for k in sorted(topological_sort.keys())]

print timeit.default_timer() - start

#################################
# input format:
# n, m
# u1 v1
# u2 v2
# s
# example:
# 5 6
# 1 2
# 1 3
# 2 3
# 2 4
# 3 5
# 4 5
# 1
# Output:
# [1, 3, 5, 2, 4]
# [1, 2, 4, 3, 5]
