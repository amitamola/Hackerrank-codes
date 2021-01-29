'''
https://www.hackerrank.com/challenges/game-of-thrones/problem
'''

import math
import os
import random
import re
import sys
from collections import Counter

def gameOfThrones(s):
    res = sum(tuple(map(lambda k:k%2, tuple(Counter(s).values()))))
    
    if res<2:
        return "YES"
    else:
        return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
