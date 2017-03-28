import timeit

start = timeit.default_timer()


# this function to read the input graph, G
def read_input():
    global n
    global m
    global edges
    global edges_reversed

    # read number of vertices - n; and
    # number of edges - m
    n, m = map(int, raw_input().strip().split(' '))

    # run loop to read all edges
    for edge in xrange(m):
        u, v = map(int, raw_input().strip().split(' '))

        # adding edge to dictionary with tail as key;
        # and all outgoing heads appended to value list
        try:
            edges[u].append(v)
        except KeyError:
            edges[u] = [v]

        try:
            edges_reversed[v].append(u)
        except KeyError:
            edges_reversed[v] = [u]


# this function is called in 1st step of Kosaraju's algorithm
# to calculate the topological order of vertices on reversed G
# Remember: Here, we are storing vertices in reversed topological
# order so they need to popped from last while running 2nd step
def dfs_reverse_graph(e):
    global set_ver_visited
    global ver_traverse_stack

    global dfs_order
    global topological_sort

    while len(ver_traverse_stack) != 0:
        # this counter checks if there are any children for each vertex
        # if no children, that's the finished time of vertex; hence
        # added to topological order
        child = 0

        # the elements are not popped from stack until there are no
        # children under it; that way, we pop them only when they are
        # finished; hence building topological order
        ver_picked = ver_traverse_stack[-1]

        if ver_picked not in dfs_order:
            dfs_order.add(ver_picked)

        try:
            vertices = e[ver_picked]
        except KeyError:
            topological_sort.append(ver_traverse_stack.pop())
            continue

        for vertex in vertices:
            if vertex not in set_ver_visited:
                set_ver_visited.add(vertex)
                ver_traverse_stack.append(vertex)
                child += 1

        # this is the time the vertex had no children, hence popped out
        # of stack and added to topological order
        if child == 0:
            topological_sort.append(ver_traverse_stack.pop())


# this function is called in 2nd step of Kosaraju's algorithm
# to calculate the SCCs
def dfs_original_graph(e):
    global set_ver_visited
    global ver_traverse_stack

    global dfs_order

    # every time DFS is called with a vertex, we keep track of all the
    # vertices it visits which is nothing but the SCC of that specific vertex
    ver_visited_temp = []

    while len(ver_traverse_stack) != 0:
        # as we are not here to build topological order, we're
        # popping element as we progress
        ver_picked = ver_traverse_stack.pop()

        dfs_order.add(ver_picked)

        try:
            vertices = e[ver_picked]
        except KeyError:
            continue

        for vertex in vertices:
            if vertex not in set_ver_visited:
                set_ver_visited.add(vertex)
                ver_traverse_stack.append(vertex)
                ver_visited_temp.append(vertex)

    return ver_visited_temp


# PROGRAM BEGINS HERE
# define variables to hold num of vertices and edges
n, m = 0, 0

# a dictionary to hold all edges of G and reversed G
edges = {}
edges_reversed = {}

# calling function that reads input
read_input()

# display G and reversed G
print "edges:", edges
print "edges reverse:", edges_reversed

# a variable to keep track of all visited vertices to ensure
# we don't process DFS for already visited vertex
set_ver_visited = set([])

# a STACK data structure to pick elements to apply DFS
ver_traverse_stack = []

# a variable to keep order of the vertices visited while applying DFS
dfs_order = set([])

# a variable to holds the topological order of vertices
topological_sort = []

# this is the 1st step of Kosaraju's algorithm:
# identify the topological order of vertices on reversed graph
# For this we run DFS on reversed G starting with highest vertex
# until the last vertex
for v in xrange(n, 0, -1):
    if v not in set_ver_visited:
        set_ver_visited.add(v)
        ver_traverse_stack.append(v)
        dfs_reverse_graph(edges_reversed)

print "REV- DFS Order:", dfs_order
print "REV- Top Order:", [topological_sort[ind] for ind in xrange(len(topological_sort) - 1, -1, -1)]

# a list to keep track of all visited vertices to ensure
# we don't process DFS for already visited vertex
set_ver_visited = set([])

# a STACK data structure to pick elements to apply DFS
ver_traverse_stack = []

# a variable to keep order of the vertices visited while applying DFS
dfs_order = set([])

# a variable to hold SCCs of G
scc = {}

# this is the 2nd step of Kosaraju's algorithm:
# identify the SCCs on original graph
# For this we run DFS on original G picking vertices in the
# topological order calculated in 1st step
while len(topological_sort) != 0:
    # Remember: 1st step stores vertices in reversed topological
    # order so they need to popped from last while running 2nd step
    v = topological_sort.pop()
    if v not in set_ver_visited:
        set_ver_visited.add(v)
        ver_traverse_stack.append(v)
        scc[v] = dfs_original_graph(edges)

print "ORG- DFS Order:", dfs_order
print "ORG- SCC:", scc

print timeit.default_timer() - start
