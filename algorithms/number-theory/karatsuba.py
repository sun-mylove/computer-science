
import timeit

start = timeit.default_timer()


def product(p, q):

    # base case to return product of two
    # single digit integers
    if p < 10 and q < 10:
        return p*q

    else:
        l1 = len(str(p))
        l2 = len(str(q))

        # calculate m from the bigger number
        # to calculate product of two integers as
        # per formula; 10^2m (ac) + 10^m ((a+b)(c+d) -ac -bd) + bd
        if l1 > l2:
            m = (l1 / 2) + (l1 % 2)
        else:
            m = (l2 / 2) + (l2 % 2)

        # splitting the given integer into two parts
        a, b = divmod(p, 10 ** m)
        c, d = divmod(q, 10 ** m)

        # printing the new numbers created by splitting the
        # original number into two parts
        # print a, b, c, d
        z1 = product(a, c)
        z3 = product(b, d)
        z2 = product(a+b, c+d) - z1 - z3

        # printing the intermediate products calculated
        # print "z1, z2, z3, m", z1, z2, z3, m

        return (10 ** (2*m)) * z1 + (10 ** m) * z2 + z3

x = 10 ** 100000
y = 10 ** 100000

print product(x, y)

stop = timeit.default_timer()

print stop - start
