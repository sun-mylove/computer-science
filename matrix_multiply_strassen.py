
import timeit

start = timeit.default_timer()


def build_matrix(M, n):
    # this function breaks a given matrix (of size n X n) into
    # 4 matrices each of size n/2 X n/2
    m1, m2, m3, m4 = [], [], [], []

    for row in xrange(0, n/2):
        for col in xrange(n/2):
            m1.append(M[(row * n) + col])

    for row in xrange(0, n/2):
        for col in xrange(n/2):
            m2.append(M[(row * n) + col + n/2])

    for row in xrange(n/2, n):
        for col in xrange(n/2):
            m3.append(M[(row * n) + col])

    for row in xrange(n/2, n):
        for col in xrange(n/2):
            m4.append(M[(row * n) + col + n/2])

    return m1, m2, m3, m4


def add(m1, m2):
    # this functions adds two given matrices and
    # returns the result
    addition = []

    for i in xrange(len(m1)):
        addition.append(m1[i] + m2[i])

    return addition


def subtract(m1, m2):
    # this functions subtracts two given matrices and
    # returns the result
    subtraction = []

    for i in xrange(len(m1)):
        subtraction.append(m1[i] - m2[i])

    return subtraction


def format_result(m1, m2, m3, m4):
    answer = []
    input_size = int(len(m1) ** 0.5)
    answer_size = len(m1) * 4
    answer_mid = len(m1) * 2

    index1, index2 = 0, 0
    while len(answer) < answer_mid:
        for i in xrange(input_size):
            answer.append(m1[index1])
            index1 += 1

        for i in xrange(input_size):
            answer.append(m2[index2])
            index2 += 1

    index1, index2 = 0, 0
    while len(answer) < answer_size:
        for i in xrange(input_size):
            answer.append(m3[index1])
            index1 += 1

        for i in xrange(input_size):
            answer.append(m4[index2])
            index2 += 1

    return answer


def matrix_multiply(X, Y, n):

    # this is the base case to return the product of two matrices
    # each of size 2 X 2
    if n == 2:
        P1 = X[0] * (Y[1] - Y[3])
        P2 = (X[0] + X[1]) * Y[3]
        P3 = (X[2] + X[3]) * Y[0]
        P4 = X[3] * (Y[2] - Y[0])
        P5 = (X[0] + X[3]) * (Y[0] + Y[3])
        P6 = (X[1] - X[3]) * (Y[2] + Y[3])
        P7 = (X[0] - X[2]) * (Y[0] + Y[1])

        # print [(P6 + P5 + P4 - P2), (P1 + P2), (P3 + P4), (P1 + P5 - P3 - P7)]
        return [(P6 + P5 + P4 - P2), (P1 + P2), (P3 + P4), (P1 + P5 - P3 - P7)]

    # this is the divide logic to divide the given matrix into 4 parts
    # recursively until the base case is hit
    else:
        # calling the function to break given matrix into
        # 4 equal sub matrices
        A, B, C, D = build_matrix(X, n)
        E, F, G, H = build_matrix(Y, n)
        # print A, B, C, D, E, F, G, H

        # calculate Strassen's 7 products as below
        P1 = matrix_multiply(A, subtract(F, H), n/2)
        P2 = matrix_multiply(add(A, B), H, n/2)
        P3 = matrix_multiply(add(C, D), E, n/2)
        P4 = matrix_multiply(D, subtract(G, E), n/2)
        P5 = matrix_multiply(add(A, D), add(E, H), n/2)
        P6 = matrix_multiply(subtract(B, D), add(G, H), n/2)
        P7 = matrix_multiply(subtract(A, C), add(E, F), n/2)

        # build the matrix of size 2 X 2 from the above 7 products
        z0 = subtract(add(add(P6, P5), P4), P2)
        z1 = add(P1, P2)
        z2 = add(P3, P4)
        z3 = subtract(add(P1, P5), add(P3, P7))

        # calling function to build the bigger matrix from 4 smaller
        # matrices by placing elements in right position
        # print z0, z1, z2, z3
        return format_result(z0, z1, z2, z3)

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 ,55, 56, 57, 58, 59, 60, 61, 62, 63, 64]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 ,55, 56, 57, 58, 59, 60, 61, 62, 63, 64]
print matrix_multiply(arr1, arr2, 8)

# arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# print matrix_multiply(arr1, arr2, 4)

stop = timeit.default_timer()

print stop - start

