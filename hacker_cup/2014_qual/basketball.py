import sys

class Player:
    def __init__(self, name, shot_pct, height):
        self.name = name
        self.shot_pct = shot_pct
        self.height = height
        self.minutes_played = 0

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "{}: {}%, {}cm".format(self.name, self.shot_pct, self.height)

    def __cmp__(self, other):
        # reverse-sort, because we want the highest values in front
        return cmp((other.shot_pct, other.height), (self.shot_pct, self.height))


def solve(M, P, players):
    players.sort()

    team1 = []
    team2 = []
    bench1 = []
    court1 = []
    bench2 = []
    court2 = []
    for i, p in enumerate(players):
        if i%2 == 0:
            team1.append(p)
        else:
            team2.append(p)

    #starting players
    for i in range(P):
        team1[i].minutes_played +=1
        team2[i].minutes_played +=1

    #for i in range(M):





    print "M: {}, P: {}".format(M,P)
    for p in team1:
        print "team1: " + str(p)
    for p in team2:
        print "team2: " + str(p)
    return 1

def sub(team, playing):
    pass

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
        N, M, P = map(int, in_file.readline().split(' '))
        # parse the rest of the input
        players = []
        for i in range(N):
            name, pct, h = in_file.readline().split(' ')
            players.append(Player(name, int(pct), int(h)))

        result = solve(M, P, players)

        print "Case #{}: {}".format(i+1, result)
