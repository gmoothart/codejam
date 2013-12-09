import sys
from random import random

# 500x500 grid for testing aaaaaa problem
f = open('aaaa_large.txt', 'w')

for y in range(500):
    for x in range(500):
        if random() < 0.15:
            f.write('#')
        else:
            f.write('.')

    f.write('\n')

f.close()

