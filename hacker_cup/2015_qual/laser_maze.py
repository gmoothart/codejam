import sys
import copy

mazes = []

def getMaze(t):
    return mazes[t%4]


def solve(maze):
    mazes.append(maze)
    mazes.append(rotate(mazes[0]))
    mazes.append(rotate(mazes[1]))
    mazes.append(rotate(mazes[2]))

    t = 0
    path = []
    current_loc = find_start(getMaze(0))
    path.append(current_loc)
    while len(path) > 0:
        if getMaze(t)[current_loc[0]][current_loc[1]] == "G":
            return t

        next_loc = find_next(current_loc, t)
        if next_loc is None:
            current_loc = path.pop()
        else:
            # mark the cell as visited at t+1 !!!!
            getMaze(t+1)[next_loc[0]][next_loc[1]] = 'x'
            current_loc = next_loc

        t += 1

    print maze
    if getMaze(t)[current_loc[0]][current_loc[1]] == "G":
        return len(path)
    
    return -1

def find_next(loc, t):
    # need a location that has not been visited in t+1, is not blocked by a laser beam at t or at t+1
    i,j = loc
    # try 'up'
    if can_visit(i-1, j, t): 
        return (i-1, j)
    # try 'right'
    if can_visit(i, j+1, t): 
        return (i, j+1)
    # try down
    if can_visit(i+1, j, t): 
        return (i+1, j)
    # try left
    if can_visit(i, j-1, t): 
        return (i, j-1)

    return None

def can_visit(i, j, t):
    M = len(getMaze(0))
    N = len(getMaze(0)[0])

    if i < 0:
        return False
    if i >= M:
        return False
    if j < 0:
        return False
    if j >= N:
        return False
    if getMaze(t+1)[i][j] != '.' and getMaze(t+1)[i][j] != 'G':
        return False
    if laser(i,j,t):
        return False
    if laser(i,j,t+1):
        return False

    return True


def laser(i,j,t):
    return False


def find_start(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                return (i, j)

def rotate(m):
    rotate_map = {
        '^': '>',
        '>': 'v',
        'v': '<',
        '<': '^',
    }
    maze = copy.deepcopy(m)


    for row in maze:
        for j in range(len(row)):
            if row[j] in rotate_map:
                row[j] = rotate_map[row[j]]

    return maze



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
        M, N = map(int, in_file.readline().split(' '))
        # parse the rest of the input
        maze = []
        for j in range(M):
            maze.append(list(in_file.readline().strip()))

        result = solve(maze)

        print "Case #{}: {}".format(i+1, "impossible" if result == -1 else str(result))
