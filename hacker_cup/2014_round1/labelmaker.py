import sys


def solve(L, labels, n):
    last_digit = ((n-1) % L)
    #result = labels[last_digit]

    #power = L
    #while n > power:
    #    next_digit = ((n-1) / power) % L 

    #    power *= L
    #    result = labels[(next_digit-1) % L] + result

    #return result
   
    
# ok, now we're getting somewhere!
    next_digit = ((n-1) / L) % L 
    next_digit2 = ((n-1) / (L * L)) % L 


    return labels[(next_digit2-1) % L] + labels[(next_digit-1) % L] + labels[last_digit]


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
        labels, n = in_file.readline().split(' ')
        n = int(n)
        # parse the rest of the input

        result = solve(len(labels), labels, n)

        print "Case #{}: {}".format(i+1, result)
