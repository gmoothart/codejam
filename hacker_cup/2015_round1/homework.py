import sys
import unittest
import math
import array


def solve(A, B, K):
    global PRIMES
    result = 0
    l = array.array('i',(0,)*(B-A+1))
    for p in PRIMES:
        if p > B:
            break

        # find first divisor
        index = A % p
        if index != 0:
            index = p - index
        #print "index {} for prime p={}".format(index, p)
        
        if index > len(l):
            continue

        for j in range(A+index, B+1, p):
            l[j-A] += 1

        #print "list = {} after prime {}".format(str(l), p)

    for i in l:
        if i == K:
            result += 1

    #print "list: {}".format(str(l))
    return result


def sieve_for_primes_to(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

class TestSolve(unittest.TestCase):

    def test_solve(self):
        self.assertEqual(5, solve(5, 15, 2))
        self.assertEqual(7, solve(2, 10, 1))
        self.assertEqual(2, solve(24, 42, 3))
        self.assertEqual(0, solve(1000000, 1000000, 1))
        self.assertEqual(1, solve(1000000, 1000000, 2))
        self.assertEqual(1, solve(7, 7, 1))
        self.assertEqual(1, solve(550, 550, 3))
        self.assertEqual(10**7, solve(2, 10**7, 1))


if __name__ == '__main__':
    global PRIMES
    PRIMES = list(sieve_for_primes_to(10 ** 7))
    #print PRIMES[:10]


    if len(sys.argv) == 1:
        unittest.main()
    else:
        # usage: $ python blank.py input.txt > output.txt
        # in python shell: >>> import blank
        #                  >>> blank.solve()
        #                  >>> reload(blank)

        #preprocess()
        #var = raw_input("Done preprocessing. press enter when file ready>")

        # open file
        try:
            in_file = open(sys.argv[1], 'r')
        except:
            print "Error opening file"
            sys.exit()

        line = in_file.readline()
        total_cases = int(line)

        for i in range(total_cases):
            # parse
            A, B, K = map(int, in_file.readline().split(' '))
            # parse the rest of the input

            result = solve(A, B, K)

            print "Case #{}: {}".format(i+1, result)
