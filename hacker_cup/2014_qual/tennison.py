import sys

cache = {}
def getkey(matches_remaining, k, ps, pr, pi, pu, pw, pd, pl):
    return "{}-{}-{}-{}-{}-{}-{}-{}-{}".format(matches_remaining, k, ps, pr, pi, pu, pw, pd, pl)

# recurse through possibilities?
def solve(matches_remaining, k, ps, pr, pi, pu, pw, pd, pl):
    key = getkey(matches_remaining, k, ps, pr, pi, pu, pw, pd, pl)
    if key in cache:
        return cache[key]

    assert matches_remaining >= k, "not winnable, why are we recurring??? m: {}, k: {}".format(matches_remaining, k)
    assert k >= 0, "invalid k:{}!".format(k)
    assert matches_remaining >= 0, "invalid m:{}!".format(matches_remaining)

    if k <= 0: return 1

    # probability of winning set is P(winning in the rain) + P(winning in the sun)
    pwinset = (pi * ps) + ((1-pi) * pr)
    plostset = 1 - pwinset

    assert pwinset >= 0 and pwinset <= 1, "ut oh. pwinset: {}, pi: {}, ps: {}, pr: {}".format(pwinset, pi, ps, pr)

    #whenever he wins a set, the probability that there will be sun increases by pu with probability pw.
    #Unfortunately, when Tennison loses a set, the probability of sun decreases by pd with probability pl.
    # update for recursive step

    # probability of winning next match is:
    # p(w) * p(won this match and p(sun) increases) + (1-p(u)) * p(won this match and p(sun) stays the same) + 
    # p(l) * p(lost this match and p(sun) decreases) + (1-p(l)) * p(lost this match and p(sun) stays the same)
    # need to weight these by p and 1-p respectively!

    # keep recursing over scenarios if it is still possible for tennison to win the match
    # that is, if matches_remaining >= k

    pwin = 0
    # can tennison still win if he loses this set?
    if matches_remaining-1 >= k:
        # tennison lost, decrease m
        pi_change = max(pi - pd, 0)
        lost_and_pi_decreases = solve(matches_remaining-1, k, ps, pr, pi_change, pu, pw, pd, pl)

        if pi_change == pi:
            # don't need to recurse here, pi didn't change so it would be duplicate work
            lost_and_pi_constant  = lost_and_pi_decreases
        else:
            lost_and_pi_constant  = solve(matches_remaining-1, k, ps, pr, pi, pu, pw, pd, pl)

        pwin = plostset * ((pl * lost_and_pi_decreases) +
                           ((1-pl) * lost_and_pi_constant))

        assert(pwin >= 0 and pwin <= 1)

    if matches_remaining >= k:
        # tennison won, decrease m and k and recur
        pi_change = min(pi + pu, 1)

        win_and_pi_increase = solve(matches_remaining-1, k-1, ps, pr, pi_change, pu, pw, pd, pl)

        if pi_change == pi:
            win_and_pi_constant = win_and_pi_increase
        else:
            win_and_pi_constant = solve(matches_remaining-1, k-1, ps, pr, pi, pu, pw, pd, pl)

        pwin = pwin + pwinset * ((pw * win_and_pi_increase) + ((1-pw) * win_and_pi_constant))
        assert(pwin >= 0 and pwin <= 1)

    cache[key] = pwin
    return pwin


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
        k, ps, pr, pi, pu, pw, pd, pl = map(float, in_file.readline().split(' '))
        k = int(k)
        # parse the rest of the input

        # it could take up to 2k-1 matches for Tennison to win k times before his opponent does
        result = solve(2*k-1, k, ps, pr, pi, pu, pw, pd, pl)

        #print "{}, {}, {}, {}, {}, {}, {}, {}".format(k, ps, pr, pi, pu, pw, pd, pl)
        print "Case #{0}: {1}".format(i+1, result)
        sys.stdout.flush()
