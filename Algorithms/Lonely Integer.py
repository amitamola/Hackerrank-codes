'''
https://www.hackerrank.com/challenges/lonely-integer/problem
'''

import math
import os
import random
import re
import sys
from collections import Counter

def lonelyinteger(a):
    return Counter(a).most_common()[-1][0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
