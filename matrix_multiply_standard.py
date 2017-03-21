
import timeit

start = timeit.default_timer()


def matrix_multiply_standard(a1, a2, p, q, r):
    answer = []

    # For a1, row = p; col = q
    # For a2, row = q, col = r
    # Outer two loops run for p, r number of times respectively;
    # p, r => size of resultant matrix
    for row in xrange(p):
        for col in xrange(r):
            value = 0

            # the loop that calculates sum of products runs for q times
            for common in xrange(q):
                # value += a1[row * col-size + col] * a2[row * col-size + col]
                value += a1[row * q + common] * a2[common * r + col]

            answer.append(value)

    return answer

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 ,55, 56, 57, 58, 59, 60, 61, 62, 63, 64]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 ,55, 56, 57, 58, 59, 60, 61, 62, 63, 64]
print matrix_multiply_standard(arr1, arr2, 8, 8, 8)

# arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# print matrix_multiply_standard(arr1, arr2, 4, 4, 4)

stop = timeit.default_timer()

print stop - start
