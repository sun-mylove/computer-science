import timeit

start = timeit.default_timer()


def fibonacci_dp(n):
    global fib_dict

    try:
        return fib_dict[n]

    except KeyError:

        if n == 1 or n == 2:
            f = 1
        else:
            f = fibonacci_dp(n - 1) + fibonacci_dp(n - 2)

        fib_dict[n] = f
        return fib_dict[n]

fib_dict = {}
print fibonacci_dp(35)

print timeit.default_timer() - start



