import timeit
import heapq

start = timeit.default_timer()


# Here we calculate the distance of each vertex from source vertex
def dijkstra(n, e, e_lengths, s):
    # dictionary that holds distance of every vertex from source vertex
    distances = {}

    # variable to hold processed vertices' distances in heap; after each iteration,
    # we pick the vertex with least distance from this heap
    ver_distances_heap = []

    # variable to keep track of vertices in heap
    ver_in_heap = set([])

    # dictionary to hold vertex --> (distance, entry) mapping
    ver_to_dist_entry = {}

    # variable to keep track of visited vertices
    ver_visited = set([])
    ver_visited.add(s)

    distances[s] = 0

    # Until the visited vertices list is filled with all vertices of G,
    # keep calculating the distance of each vertex from source vertex
    while len(ver_visited) < n:
        entry = 1

        # From each vertex in visited list, we identify all its outgoing
        # vertices.
        for ver_picked in ver_visited:
            vertices = e[ver_picked]

            # For every such outgoing vertex, we calculate its distance from
            # source vertex; if its not already in visited list and heap
            for ver in vertices:
                if ver not in ver_visited and ver not in ver_in_heap:
                    # we calculate the distance of a vertex as the distance of tail vertex
                    # plus the length of edge from tail vertex to head vertex
                    ver_distance = distances[ver_picked] + e_lengths[(ver_picked, ver)]

                    # we add each vertex's distance to a heap so we can pick vertex
                    # with minimum distance for next iteration
                    heapq.heappush(ver_distances_heap, (ver_distance, entry, ver))

                    # we keep track of vertices in heap so we don't process
                    # them again
                    ver_in_heap.add(ver)

                    # this dictionary is to pull the already calculated distance of a
                    # given vertex and its entry order
                    ver_to_dist_entry[ver] = (ver_distance, entry)

                    entry += 1

        # Once we calculate distances of all vertices, now we pick vertex
        # with minimum distance as of this point in execution; and add it to
        # visited vertices list
        if len(ver_distances_heap) > 0:
            nearest_ver_distance, trash_variable, nearest_ver = heapq.heappop(ver_distances_heap)

            # distance for given vertex from above step is final; so we add it to distances variable
            distances[nearest_ver] = nearest_ver_distance

            # adding it to vertices visited list
            ver_visited.add(nearest_ver)

            # vertex is removed from heap as this heap is to keep track of vertices
            # currently in heap only
            ver_in_heap.remove(nearest_ver)

            # This is a critical step. Here, we re-validate the distances of vertices already
            # in heap AND have an edge from the nearest_ver
            adjust_vertices = e[nearest_ver]

            for adj_ver in adjust_vertices:
                if adj_ver in ver_in_heap:
                    # taking the pre-calculated distance of given vertex
                    ver_d, ver_e = ver_to_dist_entry[adj_ver]

                    # calculating new distance from new vertex added to visited vertices list
                    new_ver_d = distances[nearest_ver] + e_lengths[(nearest_ver, adj_ver)]

                    # if the new distance is smaller, we update the heap
                    if new_ver_d < ver_d:
                        ver_distances_heap.remove((ver_d, ver_e, adj_ver))
                        heapq.heappush(ver_distances_heap, (new_ver_d, ver_e, adj_ver))

                        # update the dictionary that holds ver --> (distance,entry) as well
                        ver_to_dist_entry[adj_ver] = (new_ver_d, ver_e)

    return distances


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

    # include below block only if graph is un-directed
    try:
        edges[v].append(u)
        lengths[(v, u)] = l
    except KeyError:
        edges[v] = [u]
        lengths[(v, u)] = l

source_vertex = int(raw_input().strip())


print dijkstra(n, edges, lengths, source_vertex)

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
