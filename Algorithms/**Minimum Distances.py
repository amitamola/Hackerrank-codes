'''
https://www.hackerrank.com/challenges/minimum-distances/problem
'''

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
from collections import Counter

def mindis(a, value):
    all_ins = [i for i,val in enumerate(a) if val==value]
    
    return min([j-i for i, j in zip(all_ins[:-1], all_ins[1:])])
    

def minimumDistances(a):
    if len(set(a))==len(a):
        return -1
    
    
    else:
        oo = []
        zig = [p[0] for p in Counter(a).most_common() if p[1]>1]
        
        for all_val in zig:
            oo.append(mindis(a, all_val))
            
    return min(oo)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
