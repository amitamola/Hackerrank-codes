'''
https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
'''

import math
import os
import random
import re
import sys
from itertools import combinations

def minimumAbsoluteDifference(arr):
    mini = abs(arr[0] - arr[1])
    arr = sorted(arr)
    
    for i in range(len(arr)-1):
        absum = abs(arr[i]-arr[i+1])
        
        if absum==0:
            return 0
        
        if absum<mini:
            mini = absum
    
    return mini
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
