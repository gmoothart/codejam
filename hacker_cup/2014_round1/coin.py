import sys
from math import floor, ceil


def solve(num_jars, num_coins, goal):
    #
    # equal distribution:
    #
    min_coins = floor(float(num_coins)/num_jars)
    max_coins = ceil(float(num_coins)/num_jars)
    
    jars_with_max_coins = num_coins - (min_coins * num_jars) 
    jars_with_min_coins = int(num_jars - jars_with_max_coins)

    # each jar has the same number of coins, we can be exact
    if min_coins == max_coins:
        return goal

    # we can do it by taking the same number of coins
    # from each jar:
    if min_coins * num_jars >= goal:
        return goal

    num_wrong_guesses = jars_with_min_coins

    # worst-case incorrect guesses is jars_with_min_coins.
    # can we do better by leaving some empty jars?
    for i in range(1, int(jars_with_min_coins)):
        if num_coins % (num_jars - i) == 0:
            return i + goal

    return goal + num_wrong_guesses


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
        N, K, C = map(int, in_file.readline().split(' '))
        # parse the rest of the input

        result = solve(N, K, C)

        print "Case #{}: {}".format(i+1, result)
