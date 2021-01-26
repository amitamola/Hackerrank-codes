'''
https://www.hackerrank.com/challenges/maximizing-xor/problem
'''

import math
import os
import random
import re
import sys

def maximizingXor(l, r):
    maxi = 0
    for val in range(l,r+1):
        for val2 in range(val, r+1):
            if (val^val2)>maxi:
                maxi=val^val2
                
    return maxi

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
