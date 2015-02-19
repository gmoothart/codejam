import sys


# dumb! need to take into account not just the first digit
def solve(digits):
    # 91238: find largest!

    # find the largest
    found_larger = False
    for i, digit in enumerate(digits):
        largest_pos = i

        for j in range(i+1, len(digits)):
            if digits[j] >= digits[largest_pos]:
                largest_pos = j

        # we found one, so stop looking
        # is the stopping condition buggy?
        if largest_pos != i:
            found_larger = True
            largest_swap = (i, largest_pos)
            break

    # find the smallest
    found_smaller = False
    for i, digit in enumerate(digits):
        smallest_pos = i

        for j in range(i+1, len(digits)):
            if digits[j] > 0 and digits[j] < digits[smallest_pos]:
                smallest_pos = j

        # we found one, so stop looking
        if smallest_pos != i:
            found_smaller = True
            smallest_swap = (i, smallest_pos)
            break


    # small
    small = list(digits)
    if (found_smaller):
        tmp = small[smallest_swap[0]]
        small[smallest_swap[0]] = small[smallest_swap[1]]
        small[smallest_swap[1]] = tmp

    # large
    large = list(digits)
    if(found_larger):
        tmp = large[largest_swap[0]]
        large[largest_swap[0]] = large[largest_swap[1]]
        large[largest_swap[1]] = tmp

    #print "####### {} ####".format(digits)
    #print "largest: swap {} with {}".format(digits[0], digits[largest_pos])
    #print "smallest: swap {} with {}".format(digits[0], digits[smallest_pos])

    return (''.join(map(str, small)),
            ''.join(map(str, large)))


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
        digits = map(int, in_file.readline().strip())
        # parse the rest of the input

        result = solve(digits)

        print "Case #{}: {} {}".format(i+1, result[0], result[1])
