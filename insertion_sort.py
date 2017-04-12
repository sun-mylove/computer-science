import timeit

start = timeit.default_timer()


def insertion_sort(arr):
    # variable to hold number of swaps made during
    # sorting process; number of swaps in insertion sort
    # is same as number of swaps in bubble sort; and same
    # as number of inversions in merge sort
    total_swaps = 0

    n = len(arr)

    # Starting with 1st element (until nth element), each element is compared
    # against elements to its left until the 0th element; placing the element picked
    # in correct position

    for i in xrange(1, n):
        pivot = arr[i]

        # Below print statements show the left and right parts each
        # time pivot is selected
        # print "left", arr[:i]
        # print "right", arr[i + 1:]

        for j in xrange(i-1, -1, -1):
            if pivot < arr[j]:
                arr[j + 1] = arr[j]
                arr[j] = pivot

                total_swaps += 1

    return arr, total_swaps


inp = [6, 5, 4, 3, 2, 1]

print insertion_sort(inp)

stop = timeit.default_timer()

print stop - start

####################################
# Output:
# ([1, 2, 3, 4, 5, 6], 15)

