import timeit
import heapq

start = timeit.default_timer()


# Here we calculate the distance of each vertex from source vertex
def dijkstra(e, s):
    global n
    global distances
    global lengths

    ver_visited = set([])
    ver_visited.add(s)

    distances[s] = 0

    # Until the visited vertices list is filled with all vertices of G,
    # keep calculating the distance of each vertex from source vertex
    while len(ver_visited) < n:
        ver_lengths_heap = []
        entry = 1

        # From every vertex in visited list, we identify all its outgoing
        # vertices.
        for ver_picked in ver_visited:
            vertices = e[ver_picked]

            # For every such outgoing vertex, we calculate its distance if
            # its not already visited
            for ver in vertices:
                if ver not in ver_visited:
                    ver_length = lengths[(ver_picked, ver)] + distances[ver_picked]
                    heapq.heappush(ver_lengths_heap, (ver_length, entry, ver))
                    entry += 1

        # Once we calculate all such distances, we pick vertex with minimum
        # distance; and add it to visited vertices list
        if len(ver_lengths_heap) > 0:
            nearest_ver_tuple = heapq.heappop(ver_lengths_heap)
            nearest_ver = nearest_ver_tuple[2]
            nearest_ver_distance = nearest_ver_tuple[0]

            distances[nearest_ver] = nearest_ver_distance
            ver_visited.add(nearest_ver)


# reading num of vertices and edges
n, m = map(int, raw_input().strip().split(' '))

edges = {}
lengths = {}

# Building edges dictionary; and a dictionary with lengths
# between every two existing edges
for i in xrange(m):
    u, v, l = map(int, raw_input().strip().split(' '))

    try:
        edges[u].append(v)
        lengths[(u, v)] = l
    except KeyError:
        edges[u] = [v]
        lengths[(u, v)] = l

    try:
        edges[v].append(u)
        lengths[(v, u)] = l
    except KeyError:
        edges[v] = [u]
        lengths[(v, u)] = l

source_vertex = int(raw_input().strip())

# dictionary that holds distance of every vertex from source vertex
distances = {}
dijkstra(edges, source_vertex)

print distances

print timeit.default_timer() - start

#################################
# input format:
# n, m
# u1 v1, l1
# u2 v2, l2
# s
# example:
# 4 5
# 1 2 1
# 1 3 4
# 2 3 2
# 2 4 6
# 3 4 3
# 1
# Output:
# {1: 0, 2: 1, 3: 3, 4: 6}
