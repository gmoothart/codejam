import sys


def solve(start_radius, paint_ml):
    num_rings = 0
    paint_remaining = paint_ml

    first_circle = (start_radius + 1)**2  - start_radius**2
    if first_circle > paint_remaining:
        return 0

    paint_remaining = paint_remaining - first_circle
    outer_radius = start_radius + 1
    num_rings = num_rings + 1

    while paint_remaining >= 0:
        next_circle = (outer_radius+2)**2 - ((outer_radius+1)**2)
        #print "paint for next circle: " + str(next_circle)

        if next_circle > paint_remaining:
            return num_rings

        paint_remaining = paint_remaining - next_circle
        outer_radius = outer_radius + 2
        num_rings = num_rings + 1


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

    out_file = open('out_a.txt', 'w')
    for i in range(total_cases):
        # parse
        start_radius, paint_ml = map(int, in_file.readline().split(' '))

        result = solve(start_radius, paint_ml)

        out_file.write(("Case #{}: {}".format(i+1, result)) + "\n")
