"""
 I don't know!!!

 This is too subtle for me.
"""

fin= open("B-large-practice.in")
fout = open("out.txt", "w")

count = int(fin.readline())


def to_int_array(s):
    return [int(x) for x in s.split(' ')]

def can_mow(lawn):
    """
    rules: in a single row, height must increase.

    OR: each cell must have a "path" ?

    """
    N = len(lawn)
    M = len(lawn[0])

    # for each cell, can a legal mow be made horizontally or vertically?
    # for each interior 
    # for each diagonal, can a legal mow be made horizontally or vertically?
    for i in range(len(lawn)):
        for j in range(len(lawn[0])):
            cell = lawn[i][j]
            if not mowable(cell, lawn[i]) and not mowable(cell, [row[j] for row in lawn]):
                return "NO"

    return "YES"


def mowable(height, strip):
    # strip is "mowable" if every cell has the same height
    max_h = max(strip)
    return height == max_h


i=0
while i <= count:
    # read in one test case
    dimmension_line = fin.readline()
    n, m = to_int_array(dimmension_line)

    lawn = []
    for _ in range(n):
        lawn.append(to_int_array(fin.readline()))

    i = i+1
    result = can_mow(lawn)
    s = "Case #{}: {}".format(i, result)
    print s
    fout.write(s + "\n")


fin.close()
fout.close()
        

