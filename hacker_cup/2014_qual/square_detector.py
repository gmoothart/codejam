import sys
from math import sqrt, floor


def solve(grid):
    # first: count all octothorpes
    top, left = -1, -1
    count = 0
    for i, s in enumerate(grid):
        for j, c in enumerate(s):
            if c == '#':
                count += 1
                if top == -1:
                    top, left = i,j

    # is there the right number of octothorpes?
    side_length = sqrt(count)
    if side_length != floor(side_length):
        return "NO"

    side_length = int(side_length)

    # will the square fit?
    if top + side_length > len(grid):
        return "NO"

    if left + side_length > len(grid[0]):
        return "NO"

    print "top: {}, left: {}, side_length: {}".format(top, left, side_length)

    for i in range(top, side_length):
        for j in range(left, side_length):
            if grid[i][j] != '#':
                print "no octothorpe at {},{}".format(i,j)
                return "NO"

            print "octothorpe at {},{}".format(i,j)

    return "YES"


if __name__ == '__main__':
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
        N = int(in_file.readline())
        grid = []
        for j in range(N):
            grid.append(in_file.readline())

        result = solve(grid)

        print "Case #{}: {}".format(i+1, result)
