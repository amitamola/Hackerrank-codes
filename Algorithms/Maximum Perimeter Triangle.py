'''
https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem
'''

import math
import os
import random
import re
import sys

from itertools import combinations

def is_valid(a,b,c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return False
    else: 
        return True 

def maximumPerimeterTriangle(sticks):
    valid = []
    
    for a,b,c in set(combinations(sticks, 3)):
        if is_valid(a,b,c):
            valid.append((a,b,c))
            
    if len(valid)==0:
        return [-1]
    
    elif len(valid)==1:
        return sorted(valid[0])
        
    else:
        keep = [0,0,0]
        for v in valid:
            if sum(v)>sum(keep):
                keep = v
        return sorted(keep)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
