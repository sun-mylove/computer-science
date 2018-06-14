import timeit

start = timeit.default_timer()


def fibonacci_standard(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_standard(n - 1) + fibonacci_standard(n - 2)

print fibonacci_standard(35)

print timeit.default_timer() - start
