import timeit

start = timeit.default_timer()


def fibonacci_dp(n):
    try:
        return fib_dict[n]

    except KeyError:
        if n == 1 or n == 2:
            fib_dict[n] = 1
        else:
            fib_dict[n] = fibonacci_dp(n - 1) + fibonacci_dp(n - 2)

        return fib_dict[n]

global fib_dict
fib_dict = {}

print fibonacci_dp(35)

print timeit.default_timer() - start



