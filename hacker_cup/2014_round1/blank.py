import sys


def solve():
    return 1


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
        N, M = map(int, in_file.readline().split(' '))
        # parse the rest of the input

        result = solve()

        print "Case #{}: {}".format(i+1, result)
