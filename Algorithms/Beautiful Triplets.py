'''
https://www.hackerrank.com/challenges/beautiful-triplets/problem
'''

import math
import os
import random
import re
import sys

def beautifulTriplets(d, arr):
    count = 0
    for val in arr[:-2]:
        if (val+d) in arr and (val+2*d) in arr:
            count+=1
        else: continue
    return count   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
