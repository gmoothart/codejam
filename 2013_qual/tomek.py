def solve(board):

    # check rows
    for row in board:
        result = won(row) 
        if result: return result

    # check vertical
    for i in range(4):
        result = won([s[i] for s in board])
        if result: return result

    # check forward diagonal
    result = won([board[i][i] for i in range(4)])
    if result: return result

    # backward diagonal
    result = won([board[i][3-i] for i in range(4)])
    if result: return result

    # incomplete?
    for row in board:
        for cell in row:
            if cell == '.': return "Game has not completed"

    # draw?
    return "Draw"


def won(row):
    counts = {}
    for cell in row:
        counts[cell] = counts.get(cell,0) + 1

    if counts.get('X',0) + counts.get('T',0) == 4:
        return "X won"
    if counts.get('O',0) + counts.get('T',0) == 4:
        return "O won"

    return None


fin= open("in.txt")
fout = open("out.txt", "w")

fin.readline() # skip count


i=1
board = []
for raw_line in fin:
    line = raw_line.strip()
    if line:
        board.append(line)

    if len(board) == 4:
        result = solve(board)
        s = "Case #{}: {}".format(i, result)
        fout.write(s + '\n')
        print s

        #reinit
        board = []
        i = i+1


fin.close()
fout.close()
print "Done!"
