
import timeit

start = timeit.default_timer()


def merge_sort(alist):

    alist_length = len(alist)

    # check if the list length is less than or equal to 1
    # If yes, return that list (single element); lest call the same function
    # until the list is broken down to one element length (base case)

    if alist_length <= 1:
        return alist

    else:
        split = alist_length / 2

        left = alist[:split]
        right = alist[split:]

        if len(left) > 1:
            left = merge_sort(left)

        if len(right) > 1:
            right = merge_sort(right)

        # merge function is called with arguments, left and right halves produced
        # in that specific merge_sort function, as part of each recursive call to merge_sort

        # printing arguments to each merge call
        # print "calling merge with arguments", left, ";", right

        return merge(left, right)


def merge(l, r):

    global inversions

    l_length = len(l)
    r_length = len(r)
    i, j = 0, 0

    left_elements_added = 0

    slist = []

    # actual sort operation happens in "merge" routine
    # as part of below while and if-else blocks

    while i < l_length and j < r_length:

        if l[i] <= r[j]:
            slist.append(l[i])
            i += 1

            # this variable keeps a counter on number of elements
            # in left half added to sorted list
            left_elements_added += 1

        else:
            slist.append(r[j])
            j += 1

            # inversions is sum of number of elements in left half NOT
            # added to sorted list , every time an element from
            # right half is written to sorted list

            inversions += l_length - left_elements_added

    if i < l_length:
        while i < l_length:
            slist.append(l[i])
            i += 1
    else:
        while j < r_length:
            slist.append(r[j])
            j += 1

    # printing output of merge call
    # print "Output from merge:", slist

    return slist

# input array of integers that need to be sorted
inp = [8, 12, 5, 1, 0, 9, 3, 7]

# variable to hold number of inversions
inversions = 0

# printing sorted array
print merge_sort(inp)

# printing number of inversions
print inversions

stop = timeit.default_timer()

print stop - start
