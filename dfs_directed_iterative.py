import timeit

start = timeit.default_timer()


def dfs_directed(e, s):
    # dictionary that holds the topological sort order of vertices
    topological_sort = []

    # a list to keep track of the vertices visited applying DFS
    dfs_order = []
    set_dfs_order = set([])

    # a list to keep track of all visited vertices to ensure
    # we don't process DFS for already visited vertex
    ver_visited = set([])

    # a STACK data structure to pick elements to apply DFS
    ver_traverse_stack = []

    # initializing with starting vertex
    ver_visited.add(s)
    ver_traverse_stack.append(s)

    while len(ver_traverse_stack) != 0:
        child = 0
        ver_picked = ver_traverse_stack[-1]

        if ver_picked not in set_dfs_order:
            dfs_order.append(ver_picked)
            set_dfs_order.add(ver_picked)

        try:
            vertices = e[ver_picked]
        except KeyError:
            topological_sort.append(ver_traverse_stack.pop())
            continue

        for vertex in vertices:
            if vertex not in ver_visited:
                ver_visited.add(vertex)
                ver_traverse_stack.append(vertex)
                child += 1

        if child == 0:
            topological_sort.append(ver_traverse_stack.pop())

    # topological sort is returned in reverse order
    return dfs_order, topological_sort


# PROGRAM BEGINS HERE
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

# calling DFS algorithm
print dfs_directed(edges, starting_vertex)

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
