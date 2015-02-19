import sys


PROT = 0
CARB = 1
FAT = 2

# goal: 100 100 100 
#10 10 40
#10 30 10
#10 60 50
# call solve(100, 100, 100, [0..2]
#   call solve(90, 90, 60, [1..2]
#     call solve(80, 60, 50, [2]
#       call solve(70, 0, 0), []
#         return False
#     return False
#   call solve(90, 70, 90, [2])
#     call solve(80, 10, 40, [])
#       return False
#     
def solve(gp, gc, gf, foods):
    #print "solving for {}, {}, {}, {}".format(gp, gc, gf, foods)
    if gp == 0 and gc == 0 and gf == 0:
        #print "found a solution! {}, {}, {}, {}".format(gp, gc, gf, foods)
        return True
    if gp < 0 or gc < 0 or gf < 0:
        return False

    for i, food in enumerate(foods):
        if solve(gp-food[PROT], gc-food[CARB], gf-food[FAT], foods[i+1:]):
            return True

    return False


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
        GP, GC, GF = map(int, in_file.readline().split(' '))
        numFoods = int(in_file.readline().strip())
        foods = []
        for j in range(numFoods):
            foods.append(map(int, in_file.readline().split(' ')))

        result = solve(GP, GC, GF, foods)

        print "Case #{}: {}".format(i+1, "yes" if result else "no")
