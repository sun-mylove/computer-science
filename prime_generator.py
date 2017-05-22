import math
import timeit

start = timeit.default_timer()

base_arr = [False, False]

n = 21000
for i in range(2, n):
    base_arr.append(True)

for i in range(2, int(math.sqrt(n))):
    if base_arr[i] is True:
        j = i ** 2
        while j < n:
            base_arr[j] = False
            j += i


string_of_all_primes = ''

for i in range(n):
    if base_arr[i] is True:
        # print i
        string_of_all_primes += str(i)

print string_of_all_primes
print len(string_of_all_primes)

print timeit.default_timer() - start
