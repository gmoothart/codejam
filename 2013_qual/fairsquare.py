import math

fin= open("C-large-practice-2.in")
fout = open("out.txt", "w")

count = int(fin.readline())

LOWER = 0
UPPER = 0

def to_int_array(s):
    return [int(x) for x in s.split(' ')]


def find_palindrome_from(x):
    """
    given a number that may not be a palindrome, find the next highest
    number that is a palindrome.
    """
    if is_palindrome(x):
        x = x+1

    return x


def mod_inc(xs):

    if xs[-1] == '2':
        return int(xs) + 8

    return int(xs) + 1


def find_next_palindrome(x):
    if x <= 8: 
        return x+1
    if x == 9:
        return 11

    sx = str(x)

    # the 'bail' condition. for even numbers: 20...02
    # for odd numbers: 20...1...02
    if all(c == '2' for c in sx):
        return 10**len(sx) + 1


    mid = int(math.ceil(len(sx) / 2))
    if len(sx) % 2 == 1:
        # odd number of digits
        a,b,c = sx[0:mid], sx[mid], sx[mid+1:]

        #bail out to next power of 10?
        # numbers that look like: 2001002, 20102, 2..1..2, etc.
        if a[0] == '2' and b == '1':
            return 10**len(sx) + 1

        if int(b) < 2:
            new_b = str(mod_inc(b))
            new_a = a
        else:
            new_a = str(mod_inc(a))
            new_b = '0'
        return int(new_a + new_b + new_a[::-1])

    else:
        # even
        a,b = sx[0:mid], sx[mid:]

        #bail out to next power of 10?
        #only one of these: 2002, in general 2...2
        if a[0] == '2':
            return 10**len(sx) + 1

        new_a = str(mod_inc(a))
        return int(new_a + new_a[::-1])

def is_palindrome(x):
    sx = str(x)

    for i in range(int(math.ceil(len(sx)/2.0))):
        if sx[i] != sx[len(sx)-1-i]:
            return False

    return True


def count_fair_square(lower, upper):
    """
    Approach this backwards. Take sqrt(lower), find the next palindrome
    after it. Then keep finding next palindromes, until the square-root
    of the palindrome is greater than upper
    """
    count = 0
    x = int(math.ceil(math.sqrt(lower)))
    p = find_palindrome_from(x)
    p_squared = p**2
    while p_squared <= upper:
        if is_palindrome(p_squared):
            print "## found: ", p_squared
            count = count + 1

        p = find_next_palindrome(p)
        p_squared = p**2

    return count


cache = []
def populate_cache(upper):
    p = 1
    p_squared = p**2
    while p_squared <= upper:
        if is_palindrome(p_squared):
            cache.append(p_squared)
            print "{} -> {}".format(p, p_squared)

        p = find_next_palindrome(p)
        p_squared = p**2


def count_from_cache(lower, upper):
    counter = 0
    for i in cache:
        if i >= lower and i <= upper:
            counter = counter+1

        if i >= upper:
            break

    return counter


populate_cache(10**100)

i=1
while i <= count:
    # read in one test case
    dimmension_line = fin.readline()
    lower, upper = to_int_array(dimmension_line)

    total = count_from_cache(lower,upper)
    s = "Case #{}: {}".format(i, total)
    #print s
    fout.write(s + "\n")

    i = i+1


fin.close()
fout.close()

"""
known:
    1, 4, 9, 121, 484


1
4
9
121
484
10201
12321
14641
40804
44944
1002001
1234321
4008004
100020001
102030201
104060401
121242121
123454321
125686521
400080004
404090404
10000200001
10221412201
12102420121
12345654321


1 -> 1
2 -> 4
3 -> 9
11 -> 121
22 -> 484
101 -> 10201
111 -> 12321
121 -> 14641
202 -> 40804
212 -> 44944
1001 -> 1002001
1111 -> 1234321
2002 -> 4008004
10001 -> 100020001
10101 -> 102030201
10201 -> 104060401
11011 -> 121242121
11111 -> 123454321
11211 -> 125686521
20002 -> 400080004
20102 -> 404090404
100001 -> 10000200001
101101 -> 10221412201
110011 -> 12102420121
111111 -> 12345654321
200002 -> 40000800004
1000001 -> 1000002000001
1001001 -> 1002003002001
1002001 -> 1004006004001
1010101 -> 1020304030201
1011101 -> 1022325232201
1012101 -> 1024348434201
1100011 -> 1210024200121
1101011 -> 1212225222121
1102011 -> 1214428244121
1110111 -> 1232346432321
1111111 -> 1234567654321
2000002 -> 4000008000004
2001002 -> 4004009004004
10000001 -> 100000020000001
10011001 -> 100220141022001
10100101 -> 102012040210201
10111101 -> 102234363432201
11000011 -> 121000242000121





1 -> 1
2 -> 4
3 -> 9
11 -> 121
22 -> 484
101 -> 10201
111 -> 12321
121 -> 14641
2002 -> 4008004
10001 -> 100020001
10101 -> 102030201
10201 -> 104060401
110011 -> 12102420121
111111 -> 12345654321
200002 -> 40000800004
1000001 -> 1000002000001
1001001 -> 1002003002001
1002001 -> 1004006004001
4000000000000008000000000000004

1 -> 1
2 -> 4
3 -> 9
11 -> 121
22 -> 484
101 -> 10201
111 -> 12321
121 -> 14641
202 -> 40804
212 -> 44944
1001 -> 1002001
1111 -> 1234321
2002 -> 4008004
10001 -> 100020001
10101 -> 102030201
10201 -> 104060401
11011 -> 121242121
11111 -> 123454321
11211 -> 125686521
20002 -> 400080004
20102 -> 404090404
100001 -> 10000200001
101101 -> 10221412201
110011 -> 12102420121
111111 -> 12345654321
200002 -> 40000800004
1000001 -> 1000002000001
1001001 -> 1002003002001
1002001 -> 1004006004001
1010101 -> 1020304030201
1011101 -> 1022325232201
1012101 -> 1024348434201
1100011 -> 1210024200121
1101011 -> 1212225222121
1102011 -> 1214428244121
1110111 -> 1232346432321
1111111 -> 1234567654321
2000002 -> 4000008000004
2001002 -> 4004009004004
10000001 -> 100000020000001
10011001 -> 100220141022001
10100101 -> 102012040210201
10111101 -> 102234363432201
11000011 -> 121000242000121
"""
