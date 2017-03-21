
import timeit

start = timeit.default_timer()


def quick_sort(arr, l, r):
    if l == r:
        return arr

    elif l < r:
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp

        pivot_position = partition(arr, l, r)
        quick_sort(arr, l, pivot_position - 1)
        quick_sort(arr, pivot_position + 1, r)

    return arr


def partition(arr, l, r):
    global comparison
    comparison += r - l

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


inp = [8, 2, 1, 9, 11, 14, 0, 21, 5, 22]
comparison = 0

print quick_sort(inp, 0, len(inp) - 1)
print comparison

stop = timeit.default_timer()
print stop - start
