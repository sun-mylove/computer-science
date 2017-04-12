import timeit

start = timeit.default_timer()


def quick_sort(arr, l, r, approach):
    if l == r:
        return arr

    elif l < r:

        arr = bring_pivot_into_first_position(arr, l, r, approach)

        pivot_position = partition(arr, l, r)

        quick_sort(arr, l, pivot_position - 1, approach)
        quick_sort(arr, pivot_position + 1, r, approach)

    return arr


def bring_pivot_into_first_position(arr, l, r, appr):

    if l == r or appr == "first":
        return arr

    elif appr == "last":
        arr[l], arr[r] = arr[r], arr[l]

        return arr

    elif appr == "median":
        med = (l + r) / 2

        arr[l], arr[med] = arr[med], arr[l]

        return arr

    elif appr == "medianofthree":
        mid = (l + r) / 2
        three = [l, mid, r]
        three.sort()
        med = three[1]

        arr[l], arr[med] = arr[med], arr[l]

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

print quick_sort(inp, 0, len(inp) - 1, "first")
print comparison

stop = timeit.default_timer()
print stop - start

###############################
# Output (first):
# [0, 1, 2, 5, 8, 9, 11, 14, 21, 22]
# 21
# Output (last):
# [0, 1, 2, 5, 8, 9, 11, 14, 21, 22]
# 27
# Output (median):
# [0, 1, 2, 5, 8, 9, 11, 14, 21, 22]
# 22
# Output (medianofthree):
# [0, 1, 2, 5, 8, 9, 11, 14, 21, 22]
# 22


