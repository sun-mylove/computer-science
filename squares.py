import timeit


start = timeit.default_timer()


def find_square(prev, i):
    return prev + 2 * i + 1

inp = 81 * 99
sqr = [1]

i = 1
prev = 1
while True:
    prev = find_square(prev, i)
    if prev > inp:
        break
    sqr.append(prev)
    i += 1


print len(sqr), sqr

print timeit.default_timer() - start