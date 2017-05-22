
import timeit

start = timeit.default_timer()


def fibonacci(n):

    if n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        # calculating fibonacci in a plain recursion runs in 2^n time
        # So, calculating as per below formula (fast-doubling algorithm)
        # that runs in log(n) time:
        # If F(k) and F(k+1) are known, then
        # F(2k) = F(k) * (2 * F(k+1) - F(k))
        # F(2k+1) =  F(k+1)^2 + F(k)^2

        k = n / 2
        if n % 2 == 0:
            return fibonacci(k) * (2 * fibonacci(k + 1) - fibonacci(k))
        else:
            return fibonacci(k + 1) ** 2 + fibonacci(k) ** 2

inp = 35
print fibonacci(inp)

stop = timeit.default_timer()

print stop - start
