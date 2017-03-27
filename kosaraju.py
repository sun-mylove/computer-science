import timeit

start = timeit.default_timer()


def directed_graph_dfs(e):
    global n
    global topological_sort
    global dfs_order

    global ver_visited
    global ver_traverse_stack

    ver_visited_temp = []

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
                ver_visited_temp.append(vertex)
                child += 1

        if child == 0:
            topological_sort[n] = ver_traverse_stack.pop()
            n -= 1

    return ver_visited_temp

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

print "edges:", edges

# calculate reverse graph
edges_reversed = {}

for key in edges.keys():
    ver = edges[key]

    for v in ver:
        try:
            edges_reversed[v].append(key)
        except KeyError:
            edges_reversed[v] = [key]

print "edges reverse:", edges_reversed

# a list to keep track of all visited vertices to ensure
# we don't process DFS for already visited vertex
ver_visited = []

# a STACK data structure to pick elements to apply DFS
ver_traverse_stack = []

# dictionary that holds the topological sort order of vertices
topological_sort = {}

# a list to keep track of the vertices visited applying DFS
dfs_order = []

scc_reversed = {}

# calculate topological order for reversed graph
for v in xrange(n, 0, -1):
    if v not in ver_visited:
        ver_visited.append(v)
        ver_traverse_stack.append(v)
        scc_reversed[v] = directed_graph_dfs(edges_reversed)

print "REV- DFS Order:", dfs_order
print "REV- Top Order:", [topological_sort[k] for k in sorted(topological_sort.keys())]
print "REV- SCC:", scc_reversed

ver_traverse_order = []
for elem in [topological_sort[k] for k in sorted(topological_sort.keys())]:
    ver_traverse_order.append(elem)

print "ORIG- Order of travel:", ver_traverse_order

# a list to keep track of all visited vertices to ensure
# we don't process DFS for already visited vertex
ver_visited = []

# a STACK data structure to pick elements to apply DFS
ver_traverse_stack = []

topological_sort = {}

dfs_order = []

scc = {}

for v in ver_traverse_order:
    if v not in ver_visited:
        ver_visited.append(v)
        ver_traverse_stack.append(v)
        scc[v] = directed_graph_dfs(edges)


print "ORG- DFS Order:", dfs_order
print "ORG- Top Order:", [topological_sort[k] for k in sorted(topological_sort.keys())]
print "ORG- SCC:", scc

print timeit.default_timer() - start
