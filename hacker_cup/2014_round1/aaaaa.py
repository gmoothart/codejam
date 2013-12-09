import sys

bottommost_car = -1
rightmost_car = -1
grid = []
N=0
M=0

def key(x,y):
    return "x:{},y:{}".format(x,y)

def can_go_up(x,y, used_up, path):
    return (not used_up) and (y > 0) and (grid[y-1][x] != '#') \
        and not (key(x,y-1) in path)

def can_go_down(x,y, path):
    return y < N-1 and grid[y+1][x] != '#' \
        and not (key(x,y+1) in path)

def can_go_right(x,y, path):
    return x < M-1 and grid[y][x+1] != '#' \
        and not (key(x+1,y) in path)

def can_go_left(x,y, used_left, path):
    return (not used_left) and  x > 0 and grid[y][x-1] != '#' \
        and not (key(x-1,y) in path)

def best_from_here(x,y, used_up, used_left):
    if used_up and used_left:
        n = N - y
        m = M - x

        #print "best from {},{}: {}".format(x,y, m+n-1)
        return m + n - 1


    if used_up and not used_left:

    if not used_up and used_left:

    else not used_up and not used_left:

    return "not implemented yet"


def max_queue(x, y, used_up, used_left, path):
    # pruning ideas: 
    # can special-case a bottom-right section with no hashes in it
    # can also use that as a max value for pruning
    sizes = [0]
    #print "({}, {})".format(x,y)
    path.append( key(x,y) )

    # if there are no cars left, we can calculate the remainder in a straightforward way
    if used_up and used_left and (x > rightmost_car or y > bottommost_car):
        return best_from_here(x, y, True, True)


    # TODO: can't go up/left if we just went down
    if can_go_up(x,y,used_up, path):
        #print "going up"
        sizes.append( max_queue(x, y-1, False, True, path[:]) )

    if can_go_left(x,y,used_left, path):
        #print "going left"
        sizes.append( max_queue(x-1, y, True, False, path[:]) )

    if can_go_down(x,y, path):
        #print "going down"
        special_move = used_up or used_left
        sizes.append( max_queue(x, y+1, special_move, special_move, path[:]) )

    if can_go_right(x,y, path):
        #print "going right"
        special_move = used_up or used_left
        sizes.append( max_queue(x+1, y, special_move, special_move, path[:]) )


    #print "max queue size from {},{}: {}".format(x,y, 1+max(sizes))
    #print "path to here: {}".format(path)
    return 1 + max(sizes)


def solve():
    global bottommost_car
    global rightmost_car
    for y in range(N):
        for x in range(M):
            if grid[y][x] == '#':
                if y > bottommost_car:
                    bottommost_car = y
                if x > rightmost_car:
                    rightmost_car = x

    return max_queue(0,0, False, False, [])


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
        grid = []
        bottommost_car = -1
        rightmost_car = -1
        # parse the rest of the input
        for _ in range(N):
            grid.append(in_file.readline().strip())

        result = solve()

        print "Case #{}: {}".format(i+1, result)
