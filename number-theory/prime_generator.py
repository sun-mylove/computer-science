# refer: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

import math
import timeit

start = timeit.default_timer()


def prime_generator(n):
    # calculates all the prime numbers below n
    base_arr = [False, False]

    # initially, set all boolean values to True
    for i in range(2, n):
        base_arr.append(True)

    for i in range(2, int(math.sqrt(n))):
        if base_arr[i] is True:
            j = i ** 2
            while j < n:
                base_arr[j] = False
                j += i

    all_primes = []

    for i in range(n):
        if base_arr[i] is True:
            all_primes.append(i)

    return all_primes


print prime_generator(10000)

print timeit.default_timer() - start


