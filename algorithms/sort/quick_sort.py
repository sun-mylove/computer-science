
import timeit

start = timeit.default_timer()


def quick_sort(arr, l, r):
    if l == r:
        return arr

    elif l < r:
        print arr
        pivot_position = partition(arr, l, r)
        quick_sort(arr, l, pivot_position - 1)
        quick_sort(arr, pivot_position + 1, r)

    return arr


def partition(arr, l, r):
    global comparisons
    comparisons += r - l

    pivot = arr[l]

    i = l + 1

    for j in xrange(l + 1, r + 1):
        if arr[j] <= pivot:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1

    temp = arr[i - 1]
    arr[i - 1] = pivot
    arr[l] = temp

    return i - 1


inp = [4, 5, 3, 7, 2]
comparisons = 0

print quick_sort(inp, 0, len(inp) - 1)
print comparisons

stop = timeit.default_timer()
print stop - start
