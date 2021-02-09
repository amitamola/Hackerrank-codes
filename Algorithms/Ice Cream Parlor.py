'''
https://www.hackerrank.com/challenges/icecream-parlor/
'''

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    for it, val in enumerate(arr):
        for it2, val2 in enumerate(arr[it+1:]):
            if val+val2==m:
                return it+1, it2+it+2
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
