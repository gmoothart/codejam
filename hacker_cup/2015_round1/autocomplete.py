import sys
import unittest

class Node:
    def __init__(self, char, is_a_word):
        self.char = char
        self.children = []
        self.is_a_word = is_a_word

    def add_child(self, node):
        self.children.append(node)

def solve(words):
    l = []
    chars = 0
    trie = Node(None, False)
    for w in words:
        trie.add_child(build(w))



    p(trie)
    return chars

def build(word):
    if len(word) == 1:
        return Node(word[0], True)

    node = Node(word[0], False)
    node.add_child(build(word[1:]))
    return node

def p(trie):
    print "'{}' -> {}".format(trie.char, list(p(n) for n in trie.children))


class TestSolve(unittest.TestCase):

    def test_solve(self):
        a = ["hi", "hello", "lol", "hills", "hill"]
        self.assertEqual(11, solve(a))
        a = ["a", "aa", "aaa", "aaaa", "aaaaa"]
        self.assertEqual(11, solve(a))
        a = ["aaaaa", "aaaa", "aaa", "aa", "a"]
        self.assertEqual(11, solve(a))
        a = ["to", "be", "or", "not", "two", "bee"]
        self.assertEqual(11, solve(a))
        a = ["having", "fun", "yet"]
        self.assertEqual(11, solve(a))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        unittest.main()
    else:
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
            # parse the rest of the input

            result = solve()

            print "Case #{}: {}".format(i+1, result)
