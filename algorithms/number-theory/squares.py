import timeit


start = timeit.default_timer()


# this function finds all the squares (of natural numbers)
# that are less than given input
def next_square(prev, i):
    # (n + 1)^2 = n^2 + 2n + 1
    return prev + 2 * i + 1

inp = 100
squares = [1]

i = 1
prev = 1
while True:
    prev = next_square(prev, i)
    if prev > inp:
        break
    squares.append(prev)
    i += 1

print "Squares:", squares
print "Num of squares below %d are %d" % (inp, len(squares))

print timeit.default_timer() - start
