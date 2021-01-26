'''
https://www.hackerrank.com/challenges/priyanka-and-toys/problem
'''

import math
import os
import random
import re
import sys

def toys(w):
    w = sorted(w)
    
    f = w[0]
    cont = 1
    for it, val in enumerate(w):
        if val<=f+4:
            continue
        
        else:
            f=w[it]
            cont+=1
    return cont

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
