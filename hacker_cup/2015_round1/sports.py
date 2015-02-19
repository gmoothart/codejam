import sys
import unittest


def solve(us, them):
    global M

    stressful = M[them][them] % 1000000007
    stress_free = M[us-1][them] % 1000000007
    return (stress_free, stressful)

def computeM():
    N = 2001
    result = [[0 for x in range(N+1)] for x in range(N+1)] 
    for i in range(0,N+1):
        for j in range(0,i+1):
            if (j == 0):
                result[i][j] = 1
            else:
                result[i][j] = result[i-1][j] + result[i][j-1]

    return result

class TestSolve(unittest.TestCase):

    def test_solve(self):
        self.assertEqual((1,1), solve(2,1))
        self.assertEqual((2,1), solve(3,1))
        self.assertEqual((2,2), solve(3,2))
        self.assertEqual((1001,42), solve(10,5))
        self.assertEqual((70047606,591137401), solve(1000,500))


if __name__ == '__main__':
    global M
    M = computeM()


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
            us, them = map(int, in_file.readline().split('-'))
            # parse the rest of the input

            result = solve(us, them)

            print "Case #{}: {} {}".format(i+1, result[0], result[1])
