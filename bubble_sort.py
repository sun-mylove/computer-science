[import timeit

start = timeit.default_timer()


def bubble_sort(arr):
    # variable to hold number of swaps made during
    # sorting process; number of swaps in bubble sort
    # is same as number of inversions in merge sort
    total_swaps = 0

    n = len(arr)

    # logic to compare each element with adjacent (right) element till end of
    # the array is executed for "n-1" number of times. Each loop moves the
    # bigger number to the right of the array (so called bubble)
    for i in xrange(n-1):
        swaps = 0

        # Each element is compared against its adjacent (right) element till the
        # end of array is reached. Each such process moves the bigger number to
        # the right of the array; hence, upper bound is decremented by 1 after
        # each such process
        for j in xrange(n-1-i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

                total_swaps += 1
                swaps += 1

        # If there are no swaps in a complete traversal from left to right,
        # that implies array is sorted; hence breaking out of sorting process
        if swaps == 0:
            break

    return arr, total_swaps


inp = [5, 12, 8, 1, 0, 9, 3, 7]

print bubble_sort(inp)

stop = timeit.default_timer()

print stop - start

###################################
# Output:
# ([0, 1, 3, 5, 7, 8, 9, 12], 16)
